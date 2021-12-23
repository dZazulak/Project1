from behave import Given, When, Then


@When(u'The manager inputs an employee ID in the input')
def manager_inputs_employee_id(context):
    context.show_statistics.select_employee_id_input().send_keys(1)


@When(u'The manager clicks the Show statistics button')
def manager_clicks_statistics_button(context):
    context.show_statistics.select_show_statistics_button().click()


@Then(u'The manager page should populate wth the statistics of the employee ID entered')
def get_manager_page(context):
    context.driver.get(r"file:///C:/Users/chris/PycharmProjects/project1/front_end/html/manager_page.html")
