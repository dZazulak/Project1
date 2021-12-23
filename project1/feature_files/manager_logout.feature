Feature: Manager logout
  Scenario: As an Manager I want to be able to logout to protect my information
    Given The manager is logged in
    When The manager clicks on the logout button
    Then The manager will return to the login page and have to log back in to view his reimbursements