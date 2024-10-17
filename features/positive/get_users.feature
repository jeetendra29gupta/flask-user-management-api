Feature: User Management API - Get Users

  @get_users
  Scenario: Get all users successfully
    Given the API is running
    When I request all users
    Then the response status should be 200
    And the response should be a list of users
