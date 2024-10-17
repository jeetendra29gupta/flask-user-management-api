Feature: User Management API - Error Handling

  @get_user_error_handling
  Scenario: Fail to get a user by non-existent ID
    Given the API is running
    When I request a user by ID 999
    Then the response status should be 404
    And the response message should be "User not found"

  @delete_user_error_handling
  Scenario: Fail to delete a non-existent user
    Given the API is running
    When I delete the user with ID 999
    Then the response status should be 404
    And the response message should be "User not found"

  @update_user_error_handling
  Scenario: Fail to update a non-existent user
    Given the API is running
    When I update the user with ID 999
    Then the response status should be 404
    And the response message should be "User not found"

  @partial_update_user_error_handling
  Scenario: Fail to partially update a non-existent user
    Given the API is running
    When I partially update the user with ID 999
    Then the response status should be 404
    And the response message should be "User not found"
