from behave import Given, When, Then


@Given(u'The manager is logged in')
def get_manager_page(context):
    context.driver.get(r"file:///C:/Users/chris/PycharmProjects/project1/front_end/html/manager_page.html")


@When(u'The manager clicks on the logout button')
def manager_clicks_logout(context):
    context.manager_logout.select_manager_logout_button().click()


@Then(u'The manager will return to the login page and have to log back in to view his reimbursements')
def step_impl(context):
    assert context.driver.title == "Login"
