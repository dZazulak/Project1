from behave import Given, When, Then


@Given(u'the employee is on the login page')
def get_login_page(context):
    context.driver.get(r"file:///C:/Users/chris/PycharmProjects/project1/front_end/html/login_page.html")


@When(u'the employee enters their {username} in the username input box')
def employee_enters_email(context, username: str):
    context.login_page.select_email_input().send_keys(username)


@When(u'the employee enters their {password} in the password input box')
def employee_enters_password(context, password: str):
    context.login_page.select_password_input().send_keys(password)


@When(u'employee clicks the login button')
def employee_clicks_login_button(context):
    context.login_page.select_login_button().click()


@Then(u'the employee should be logged in and redirected to the employee home page')
def redirected_to_employee_page(context):
    context.driver.get(r"file:///C:/Users/chris/PycharmProjects/project1/front_end/html/employee_page.html")
