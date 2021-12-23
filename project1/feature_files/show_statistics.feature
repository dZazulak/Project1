Feature: Employee statistics
  Scenario: As the manager, I want to be able to view statistics on each employee
    Given The manager is logged in
    When The manager inputs an employee ID in the input
    When The manager clicks the Show statistics button
    Then The manager page should populate wth the statistics of the employee ID entered
