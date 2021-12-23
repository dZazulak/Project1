Feature: The employee should be able to login when using a correct email and password


  Scenario Outline: As an employee I want to login so that I can manage my reimbursements
    Given the employee is on the login page
    When the employee enters their <username> in the username input box
    When the employee enters their <password> in the password input box
    When employee clicks the login button
    Then the employee should be logged in and redirected to the employee home page

    Examples:
      | username                  | password |
#      | alex.lara@shield.inc | aa       |
#      | alex.lara@shield.com | alex     |
      | alex.lara@shield.inc      | alex     |
      | eric.jennings@shield.inc  | eric     |
      | victor.herrera@shield.inc | victor   |