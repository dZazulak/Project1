from behave import Given, Then, When


@When(u'The employee enters their <managerId> into the manager ID input for reject')
def manager_id_input_reject(context, manager_id: int):
    context.reject_create_reimbursement.manager_id_input().send_keys(manager_id)


@When(u'The employee inputs a {negative} reimbursement amount')
def employee_inputs_negative_amount(context, negative: int):
    context.reject_create_reimbursement.negative_amount_input().send_keys(negative)


@Then(u'The system should alert the user that the amount is invalid')
def system_alert_invalid_amount(context):
    context.driver.implicitly_wait(2)
    assert context.driver.switch_to.alert.text == "There was an issue"
