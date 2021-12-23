import time

from behave import Given, When, Then


@Given(u'The manager is on the manager page')
def get_manager_page(context):
    context.driver.get(r"file:///C:/Users/chris/PycharmProjects/project1/front_end/html/manager_page.html")


@When(u'The manager inputs a {comment} into the Approve manager comment input')
def manager_input_comment(context, comment: str):
    time.sleep(1)
    context.approve_reimbursement.select_manager_approve_comment_input().send_keys(comment)


@When(u'The manager clicks on the Approve button')
def manager_click_approve(context):
    context.approve_reimbursement.select_approve_button().click()


@Then(u'The manager page should refresh and the reimbursement moved to the past reimbursements section')
def manager_retrieve_manager_page(context):
    context.driver.get(r"file:///C:/Users/chris/PycharmProjects/project1/front_end/html/manager_page.html")
