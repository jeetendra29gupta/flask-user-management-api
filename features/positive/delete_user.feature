Feature: User Management API - Delete User

  @delete_user
  Scenario: Delete a user successfully
    Given the API is running
    Given a user exists with ID 4
    When I delete the that user
    Then the response status should be 200
    And the response message should be "User deleted successfully"
