from behave import Given, When, Then


@Given(u'The employee is logged in and on the employee home page')
def get_employee_page(context):
    context.driver.get(r"file:///C:/Users/chris/PycharmProjects/project1/front_end/html/employee_page.html")


@When(u'The employee clicks on the new reimbursement button')
def employee_clicks_new_reimbursement_button(context):
    context.create_reimbursement_page.select_create_reimbursement_button().click()


@When(u'The employee is redirected to the reimbursement page')
def get_new_reimbursement_page(context):
    context.driver.get(r"file:///C:/Users/chris/PycharmProjects/project1/front_end/html/reimbursement_page.html")


@When(u'The employee enters their {managerId} into the manager ID input')
def employee_enters_managerId(context, managerId: int):
    context.create_reimbursement_page.select_managerId_input().send_keys(managerId)


@When(u'The employee enters an {amount} into the amount input')
def employee_enters_amount(context, amount: int):
    context.create_reimbursement_page.select_amount_input().send_keys(amount)


@When(u'The employee enters a {message} into the reason input')
def employee_enters_message(context, message: str):
    context.create_reimbursement_page.select_message_input().send_keys(message)


@When(u'The employee clicks the submit reimbursement button')
def employee_clicks_submit_reimbursement_button(context):
    context.create_reimbursement_page.select_submit_button().click()


@Then(u'The form should disappear and load the employee page with the new reimbursement')
def redirected_to_employee_page(context):
    context.driver.get(r"file:///C:/Users/chris/PycharmProjects/project1/front_end/html/employee_page.html")
