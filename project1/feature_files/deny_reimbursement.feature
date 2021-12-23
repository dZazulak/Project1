Feature: Approve Reimbursement
  Scenario Outline: As a manager I want to deny any reimbursement that I believe is legitimate
    Given the manager is on the login page
    When the manager enters their <username> in the username input box
    When the manager enters their <password> in the password input box
    When manager clicks the login button
    When The manager inputs a <comment> into the Deny manager comment input
    When The manager clicks on the Deny button
    Then The manager page should refresh and the reimbursement moved to the past reimbursements section
    Examples:
      | username                 | password | comment             |
      | eric.suminski@shield.inc | eric     | Denied by selenium. |