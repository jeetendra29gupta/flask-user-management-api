from flask import Blueprint, request, jsonify

from database import Session
from models import User

user_bp = Blueprint('user_bp', __name__)

health_bp = Blueprint('health_bp', __name__)


@health_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health Check
    ---
    tags:
      - health
    responses:
      200:
        description: Service is healthy
      500:
        description: Service is unhealthy
    """
    try:
        # Here you could add additional checks, e.g., database connection check
        return jsonify({'status': 'healthy'}), 200
    except Exception as ex:
        return jsonify({'status': 'unhealthy', 'error': str(ex)}), 500


# Create a new user
@user_bp.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user
    ---
    tags:
      - users
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: User
          required:
            - username
            - email
            - salary
          properties:
            username:
              type: string
              description: The name of the user
            email:
              type: string
              description: The email of the user
            salary:
              type: number
              description: The salary of the user
    responses:
      201:
        description: User created successfully
      400:
        description: Bad request - missing or invalid parameters.
      500:
        description: Internal server error occurred.
    """
    try:
        data = request.get_json()
        if not all(key in data for key in ['username', 'email', 'salary']):
            return jsonify({'message': 'Missing required parameters'}), 400

        with Session() as session:
            new_user = User(username=data['username'], email=data['email'], salary=data['salary'])
            session.add(new_user)
            session.commit()

        return jsonify({'message': 'user created'}), 201

    except Exception as ex:
        return jsonify({'message': 'Internal server error occurred', 'error': str(ex)}), 500


# Get all users
@user_bp.route('/users', methods=['GET'])
def get_users():
    """
    Get all users
    ---
    tags:
      - users
    responses:
      200:
        description: A list of users
        schema:
          type: array
          items:
            $ref: '#/definitions/User'
      500:
        description: Internal server error occurred.
    """
    try:
        with Session() as session:
            users = session.query(User).all()
            return jsonify(
                [{'user_id': user.user_id, 'username': user.username, 'email': user.email, 'salary': user.salary} for
                 user in users]), 200

    except Exception as ex:
        return jsonify({'message': 'Internal server error occurred', 'error': str(ex)}), 500


# Get user by ID
@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get user by ID
    ---
    tags:
      - users
    parameters:
      - name: user_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: User found
        schema:
          type: object
          properties:
            user_id:
              type: integer
            username:
              type: string
            email:
              type: string
            salary:
              type: number
      404:
        description: User not found
      500:
        description: Internal server error occurred.
    """
    try:
        with Session() as session:
            user = session.query(User).filter(User.user_id == user_id).first()
            if user is None:
                return jsonify({'message': 'User not found'}), 404

            return jsonify(
                {'user_id': user.user_id, 'username': user.username, 'email': user.email, 'salary': user.salary}), 200

    except Exception as ex:
        return jsonify({'message': 'Internal server error occurred', 'error': str(ex)}), 500


# Update a user by ID
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update a user by ID
    ---
    tags:
      - users
    parameters:
      - name: user_id
        in: path
        required: true
        type: integer
      - name: body
        in: body
        required: true
        schema:
          id: User
          required:
            - username
            - email
            - salary
          properties:
            username:
              type: string
              description: The name of the user
            email:
              type: string
              description: The email of the user
            salary:
              type: number
              description: The salary of the user
    responses:
      200:
        description: User updated successfully
      400:
        description: Bad request - missing or invalid parameters.
      404:
        description: User not found
      500:
        description: Internal server error occurred.
    """
    try:
        data = request.get_json()

        if not all(key in data for key in ['username', 'email', 'salary']):
            return jsonify({'message': 'Missing required parameters'}), 400

        with Session() as session:
            user = session.query(User).filter(User.user_id == user_id).first()
            if user is None:
                return jsonify({'message': 'User not found'}), 404

            user.username = data['username']
            user.email = data['email']
            user.salary = data['salary']
            session.commit()

        return jsonify({'message': 'User updated successfully'}), 200

    except Exception as ex:
        return jsonify({'message': 'Internal server error occurred', 'error': str(ex)}), 500


# Delete a user by ID
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user by ID
    ---
    tags:
      - users
    parameters:
      - name: user_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
      500:
        description: Internal server error occurred.
    """
    try:
        with Session() as session:
            user = session.query(User).filter(User.user_id == user_id).first()
            if user is None:
                return jsonify({'message': 'User not found'}), 404

            session.delete(user)
            session.commit()

        return jsonify({'message': 'User deleted successfully'}), 200

    except Exception as ex:
        return jsonify({'message': 'Internal server error occurred', 'error': str(ex)}), 500


# Partially update a user by ID
@user_bp.route('/users/<int:user_id>', methods=['PATCH'])
def partial_update_user(user_id):
    """
    Partially update a user by ID
    ---
    tags:
      - users
    parameters:
      - name: user_id
        in: path
        required: true
        type: integer
      - name: body
        in: body
        required: false
        schema:
          id: User
          properties:
            username:
              type: string
              description: The name of the user
            email:
              type: string
              description: The email of the user
            salary:
              type: number
              description: The salary of the user
    responses:
      200:
        description: User partially updated successfully
      400:
        description: Bad request - missing or invalid parameters.
      404:
        description: User not found
      500:
        description: Internal server error occurred.
    """
    try:
        data = request.get_json()

        if not any(key in data for key in ['username', 'email', 'salary']):
            return jsonify({'message': 'Missing required parameters'}), 400

        with Session() as session:
            user = session.query(User).filter(User.user_id == user_id).first()
            if user is None:
                return jsonify({'message': 'User not found'}), 404

            if 'username' in data:
                user.username = data['username']
            if 'email' in data:
                user.email = data['email']
            if 'salary' in data:
                user.salary = data['salary']

            session.commit()

        return jsonify({'message': 'User partially updated successfully'}), 200

    except Exception as ex:
        return jsonify({'message': 'Internal server error occurred', 'error': str(ex)}), 500
