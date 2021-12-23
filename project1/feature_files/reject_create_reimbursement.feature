Feature: Invalid reimbursement amount
  Scenario Outline: As the system, I should deny any attempt at a negative or non-numeric reimbursement amount
    Given the employee is on the login page
    When the employee enters their <username> in the username input box
    When the employee enters their <password> in the password input box
    When The employee enters their <managerId> into the manager ID input for reject
    When The employee inputs a <negative> reimbursement amount
    When The employee enters a <message> into the reason input
    When The employee clicks the submit reimbursement button
    Then The system should alert the user that the amount is invalid
    Examples:
      | username             | password | managerId | negative | message  |
      | alex.lara@shield.inc | alex     | 2         | -500     | Negative |