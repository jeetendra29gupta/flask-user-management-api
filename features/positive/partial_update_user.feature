Feature: User Management API - Partial Update User

  @partial_update_user
  Scenario: Partially update a user successfully
    Given the API is running
    Given a user exists with ID 3
    When I partially update the user with username "blue_bird_1814"
    Then the response status should be 200
    And the response message should be "User partially updated successfully"
