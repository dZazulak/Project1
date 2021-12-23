Feature: Approve Reimbursement
  Scenario Outline: As a manager I want to approve any reimbursement that I believe is legitimate
    Given the manager is on the login page
    When the manager enters their <username> in the username input box
    When the manager enters their <password> in the password input box
    When manager clicks the login button
    When The manager inputs a <comment> into the Approve manager comment input
    When The manager clicks on the Approve button
    Then The manager page should refresh and the reimbursement moved to the past reimbursements section

        Examples:
          | comment        | username                 | password |
          | Did this work? | eric.suminski@shield.inc | eric     |