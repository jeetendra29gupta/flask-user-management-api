Feature: User Management API - Get User by ID

  @get_user_by_id
  Scenario: Get user by ID successfully
    Given the API is running
    Given a user exists with ID 1
    When I request that user
    Then the response status should be 200
    And the user details should include username "juju_raven_1814"
