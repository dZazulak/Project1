import time

from behave import Given, When, Then


@When(u'The manager inputs a {comment} into the Deny manager comment input')
def manager_input_comment(context, comment: str):
    time.sleep(1)
    context.deny_reimbursement.select_manager_deny_comment_input().send_keys(comment)


@When(u'The manager clicks on the Deny button')
def manager_click_approve(context):
    context.deny_reimbursement.select_deny_button().click()
