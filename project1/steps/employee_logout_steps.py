from behave import Given, When, Then

@Given(u'The employee is logged in')
def get_employee_page(context):
    context.driver.get(r"file:///C:/Users/chris/PycharmProjects/project1/front_end/html/employee_page.html")


@When(u'The employee clicks on the logout button')
def employee_click_logout(context):
    context.employee_logout.select_employee_logout_button().click()


@Then(u'The employee will return to the login page and have to log back in to view his reimbursements')
def get_login_page(context):
    assert context.driver.title == "Login"
