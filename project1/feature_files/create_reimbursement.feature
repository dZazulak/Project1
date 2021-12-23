Feature: Interact with reimbursements


  Scenario Outline: As an employee I want to submit a reimbursement
    Given The employee is logged in and on the employee home page
    When The employee clicks on the new reimbursement button
    When The employee is redirected to the reimbursement page
    When The employee enters their <managerId> into the manager ID input
    When The employee enters an <amount> into the amount input
    When The employee enters a <message> into the reason input
    When The employee clicks the submit reimbursement button
    Then The form should disappear and load the employee page with the new reimbursement

    Examples:
      | managerId | amount | message                                   |
      | 1         | 1000   | Christmas bonuses for the other employees |
      | 2         | 50     | Coffee run                                |
      | 2         | 20     | Lunch                                     |