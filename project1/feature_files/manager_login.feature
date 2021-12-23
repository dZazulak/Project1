Feature: Manager login



  Scenario Outline: As an manager I want to login so that I can manage my reimbursements
    Given the manager is on the login page
    When the manager enters their <username> in the username input box
    When the manager enters their <password> in the password input box
    When manager clicks the login button
    Then the manager should be logged in and redirected to the employee home page

    Examples:
      | username                 | password |
      | eric.suminski@shield.inc | eric     |
      | david.zazulak@shield.inc | david    |