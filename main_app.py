from flasgger import Swagger
from flask import Flask

from database import init_db
from routes import user_bp, health_bp

app = Flask(__name__)

# Initialize Swagger
swagger = Swagger(app)

# Initialize the database
init_db()

# Register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(health_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)
