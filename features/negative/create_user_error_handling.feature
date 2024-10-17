Feature: User Management API - Create User Error Handling

  @create_user_error_handling_1
  Scenario: Fail to create a new user due to missing parameters
    Given the API is running
    When I create a new user with username "juju_raven_1814" and salary 500
    Then the response status should be 400
    And the response message should be "Missing required parameters"

  @create_user_error_handling_2
  Scenario: Fail to create a new user due to missing parameters
    Given the API is running
    When I create a new user with username "juju_raven_1814" and email "jeetendra.gupta@gmail.com"
    Then the response status should be 400
    And the response message should be "Missing required parameters"

  @create_user_error_handling_3
  Scenario: Fail to create a new user due to missing parameters
    Given the API is running
    When I create a new user with email "jeetendra.gupta@gmail.com" and salary 500
    Then the response status should be 400
    And the response message should be "Missing required parameters"
