Feature: User Management API - Update User

  @update_user
  Scenario: Update a user successfully
    Given the API is running
    Given a user exists with ID 2
    When I update the user with username "black_rose_1814", email "prince.gupta@gmail.com", and salary 200
    Then the response status should be 200
    And the response message should be "User updated successfully"
