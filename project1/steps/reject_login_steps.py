from behave import Given, When, Then


@Given(u'User is on the login page')
def get_login_page(context):
    context.driver.get(r"file:///C:/Users/chris/PycharmProjects/project1/front_end/html/login_page.html")


@When(u'The user inputs an incorrect email into the email input box')
def incorrect_email_input(context):
    context.reject_login.select_email_input().send_keys("dave")


@When(u'The user inputs an incorrect password into the password input box')
def incorrect_password_input(context):
    context.reject_login.select_password_input().send_keys("abc")


@Then(u'The system should alert the user that the email/password was incorrect')
def alert_failed_login(context):
    context.driver.implicitly_wait(2)
    assert context.driver.switch_to.alert.text == "Invalid username or password"
    context.driver.switch_to.alert.accept()
