Feature: Employee logout
  Scenario: As an employee I want to be able to logout to protect my information
    Given The employee is logged in
    When The employee clicks on the logout button
    Then The employee will return to the login page and have to log back in to view his reimbursements
