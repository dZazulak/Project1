from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp
from entities.reimbursement import Reimbursement

reimbursement_dao = ReimbursementDAOImp()

employee_reimbursement = Reimbursement(0, 1, 2, 50, "Pending", "Test Reimbursement", "")
approve_reimbursement = Reimbursement(4, 3, 1, 500, "Approved", "New Work Laptop", "Approving Reimbursement")
deny_reimbursement = Reimbursement(3, 3, 1, 5, "Denied", "Snacks", "")
comment_reimbursement = Reimbursement(3, 3, 1, 5, "Denied", "Snacks",
                                      "Snacks are not a good reason for a reimbursement")


def test_get_reimbursement_by_id_success():
    returned_reimbursement: Reimbursement = reimbursement_dao.get_reimbursement_by_id(1)
    assert returned_reimbursement.reimbursement_id == 1


def test_get_all_reimbursement_success():
    reimbursement_list = reimbursement_dao.get_all_reimbursements_by_id()
    assert len(reimbursement_list) >= 2


def test_get_all_reimbursements_by_employee_id_success():
    employee_reimbursement_list = reimbursement_dao.get_all_reimbursements_by_employee_id(3)
    assert len(employee_reimbursement_list) >= 1


# def test_get_reimbursement_by_approval_success():
#     returned_reimbursement_by_approval: Reimbursement = reimbursement_dao.get_reimbursement_by_approval(2, "Pending")
#     assert returned_reimbursement_by_approval.employee_id == 2
#
#
# def test_get_all_reimbursements_by_approval_success():
#     approval_reimbursement_list = reimbursement_dao.get_all_reimbursements_by_approval("Pending")
#     assert len(approval_reimbursement_list) >= 2


def test_approve_reimbursement_success():
    approved_reimbursement: Reimbursement = reimbursement_dao.approve_reimbursement(approve_reimbursement)
    assert approved_reimbursement.approval


def test_deny_reimbursement_success():
    denied_reimbursement: Reimbursement = reimbursement_dao.deny_reimbursement(deny_reimbursement)
    assert denied_reimbursement.approval


# def test_comment_on_approved_reimbursement_success():
#     commented_reimbursement: Reimbursement = reimbursement_dao.leave_comment_on_reimbursement(approve_reimbursement)
#     assert commented_reimbursement.manager_comment
#
#
# def test_comment_on_denied_reimbursement_success():
#     commented_reimbursement: Reimbursement = reimbursement_dao.leave_comment_on_reimbursement(deny_reimbursement)
#     assert commented_reimbursement.manager_comment


def test_get_all_pending_reimbursement_by_manager_id_success():
    pending_reimbursements_list: list[Reimbursement] = reimbursement_dao.get_all_pending_reimbursements_by_manager_id(2)
    assert len(pending_reimbursements_list) >= 1


def test_get_past_reimbursements_by_manager_id_success():
    past_reimbursements_list: list[Reimbursement] = reimbursement_dao.get_past_reimbursements_by_manager_id(1)
    assert len(past_reimbursements_list) >= 1


def test_create_new_reimbursement_by_employee_id_success():
    new_reimbursement: Reimbursement = reimbursement_dao.create_new_reimbursement_by_employee_id(employee_reimbursement)
    assert new_reimbursement.reimbursement_id != 0
