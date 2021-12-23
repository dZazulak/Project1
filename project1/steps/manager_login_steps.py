from behave import Given, When, Then


@Given(u'the manager is on the login page')
def get_login_page(context):
    context.driver.get(r"file:///C:/Users/chris/PycharmProjects/project1/front_end/html/login_page.html")


@When(u'the manager enters their {username} in the username input box')
def manager_enters_email(context, username: str):
    context.login_page.select_email_input().send_keys(username)


@When(u'the manager enters their {password} in the password input box')
def manager_enters_password(context, password: str):
    context.login_page.select_password_input().send_keys(password)


@When(u'manager clicks the login button')
def manager_clicks_login_button(context):
    context.login_page.select_login_button().click()


@Then(u'the manager should be logged in and redirected to the employee home page')
def redirected_to_manager_page(context):
    context.driver.get(r"file:///C:/Users/chris/PycharmProjects/project1/front_end/html/manager_page.html")
