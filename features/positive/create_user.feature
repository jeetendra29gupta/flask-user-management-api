Feature: User Management API - Create User

  @create_user
  Scenario Outline: Create a new user successfully
    Given the API is running
    When I create a new user with username "<username>", email "<email>", and salary <salary>
    Then the response status should be 201
    And the response message should be "user created"

  Examples:
    | username           | email                     | salary |
    | juju_raven_1814    | jeetendra.gupta@gmail.com | 200    |
    | black_rose_1814    | prince.gupta@gmail.com    | 100    |
    | blue_bird          | sameer.gupta@gmail.com    | 200    |
    | delete_me          | delete_me@gmail.com       | 200    |
