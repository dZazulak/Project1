from custom_exceptions.duplicate_reimbursement_id_exception import DuplicateReimbursementIdException
from custom_exceptions.employee_id_not_found_exception import EmployeeIdNotFoundException
from custom_exceptions.invalid_approval_statement_exception import InvalidApprovalStatementException
from custom_exceptions.manager_id_not_found_exception import ManagerIdNotFoundException
from custom_exceptions.negative_reimbursement_exception import NegativeReimbursementException
from custom_exceptions.non_numeric_reimbursement_amount_exception import NonNumericReimbursementAmountException
from custom_exceptions.reimbursement_not_found_exception import ReimbursementNotFoundException
from custom_exceptions.too_many_characters_in_comment_exception import TooManyCharactersInCommentException
from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp
from entities.reimbursement import Reimbursement
from service_layer.implementation_services.reimbursement_service_imp import ReimbursementServiceImp

reimbursement_dao = ReimbursementDAOImp()
reimbursement_service = ReimbursementServiceImp(reimbursement_dao)

reimbursement_with_bad_approval = Reimbursement(4, 3, 1, 500, "Test", "Test Reimbursement", "")
reimbursement_with_bad_manager_id = Reimbursement(4, 3, 2, 50, "Approved", "Test Reimbursement", "")
reimbursement_with_bad_employee_id = Reimbursement(4, 500000, 1, 50, "Approved", "Test Reimbursement", "")
reimbursement_with_negative_number = Reimbursement(4, 3, 1, -500, "Pending", "New Work Laptop", "")
reimbursement_with_non_numeric = Reimbursement(4, 3, 1, "abc", "Pending", "New Work Laptop", "")
reimbursement_with_too_many_chars = Reimbursement(4, 3, 1, 500, "Approved", "Test", "123456789012345678901234567890"
                                                                                    "123456789012345678901234567890"
                                                                                    "123456789012345678901234567890"
                                                                                    "123456789012345678901234567890"
                                                                                    "123456789012345678901234567890"
                                                                                    "123456789012345678901234567890"
                                                                                    "123456789012345678901234567890"
                                                                                    "123456789012345678901234567890")
reimbursement_with_duplicate_reimbursement_id = Reimbursement(4, 3, 1, 500, "Pending", "Testing", "")


def test_get_reimbursement_by_id_fail():
    try:
        reimbursement_service.service_get_reimbursement_by_id(100000)
        assert False
    except ReimbursementNotFoundException as e:
        assert str(e) == "Reimbursement ID was not found"


def test_get_all_reimbursements_by_employee_id_fail():
    try:
        reimbursement_service.service_get_all_reimbursements_by_employee_id(50000)
        assert False
    except EmployeeIdNotFoundException as e:
        assert str(e) == "Employee ID was not found"


def test_get_reimbursement_by_approval_employee_id_fail():
    try:
        reimbursement_service.service_get_reimbursement_by_approval(1000000000, "Pending")
        assert False
    except EmployeeIdNotFoundException as e:
        assert str(e) == "Employee ID was not found"


def test_get_reimbursement_by_approval_fail():
    try:
        reimbursement_service.service_get_reimbursement_by_approval(1, "Testing")
        assert False
    except InvalidApprovalStatementException as e:
        assert str(e) == "Invalid approval"


def test_get_all_reimbursements_by_approval_fail():
    try:
        reimbursement_service.service_get_all_reimbursements_by_approval("Test")
        assert False
    except InvalidApprovalStatementException as e:
        assert str(e) == "Invalid approval"


def test_approve_reimbursement_fail_by_approval():
    try:
        reimbursement_service.service_approve_reimbursement(reimbursement_with_bad_approval)
        assert False
    except InvalidApprovalStatementException as e:
        assert str(e) == "Invalid approval"


def test_approve_reimbursement_fail_by_manager_id():
    try:
        reimbursement_service.service_approve_reimbursement(reimbursement_with_bad_manager_id)
        assert False
    except ManagerIdNotFoundException as e:
        assert str(e) == "Manager ID was not found"


def test_approve_reimbursement_fail_by_employee_id():
    try:
        reimbursement_service.service_approve_reimbursement(reimbursement_with_bad_employee_id)
        assert False
    except EmployeeIdNotFoundException as e:
        assert str(e) == "Employee ID was not found"


def test_deny_reimbursement_fail_by_approval():
    try:
        reimbursement_service.service_deny_reimbursement(reimbursement_with_bad_approval)
        assert False
    except InvalidApprovalStatementException as e:
        assert str(e) == "Invalid approval"


def test_deny_reimbursement_fail_by_manager_id():
    try:
        reimbursement_service.service_deny_reimbursement(reimbursement_with_bad_manager_id)
        assert False
    except ManagerIdNotFoundException as e:
        assert str(e) == "Manager ID was not found"


def test_deny_reimbursement_fail_by_employee_id():
    try:
        reimbursement_service.service_deny_reimbursement(reimbursement_with_bad_employee_id)
        assert False
    except EmployeeIdNotFoundException as e:
        assert str(e) == "Employee ID was not found"


def test_approve_reimbursement_comment_fail_by_manager_id():
    try:
        reimbursement_service.service_leave_comment_on_reimbursement(reimbursement_with_bad_manager_id)
        assert False
    except ManagerIdNotFoundException as e:
        assert str(e) == "Manager ID was not found"


def test_approve_reimbursement_comment_fail_by_employee_id():
    try:
        reimbursement_service.service_leave_comment_on_reimbursement(reimbursement_with_bad_employee_id)
        assert False
    except EmployeeIdNotFoundException as e:
        assert str(e) == "Employee ID was not found"


def test_approve_reimbursement_comment_fail_by_too_many_characters():
    try:
        reimbursement_service.service_leave_comment_on_reimbursement(reimbursement_with_too_many_chars)
        assert False
    except TooManyCharactersInCommentException as e:
        assert str(e) == "Too many characters"


def test_get_all_pending_approvals_fail_by_manager_id():
    try:
        reimbursement_service.service_get_all_pending_reimbursements_by_manager_id(50000)
        assert False
    except ManagerIdNotFoundException as e:
        assert str(e) == "Manager ID was not found"


def test_get_all_past_approvals_fail_by_manager_id():
    try:
        reimbursement_service.service_get_past_reimbursements_by_manager_id(50000)
        assert False
    except ManagerIdNotFoundException as e:
        assert str(e) == "Manager ID was not found"


def test_invalid_approval_statement_create_reimbursement_fail():
    try:
        reimbursement_service.service_create_new_reimbursement_by_employee_id(reimbursement_with_bad_approval)
        assert False
    except InvalidApprovalStatementException as e:
        assert str(e) == "Invalid approval"


def test_invalid_amount_negative_fail():
    try:
        reimbursement_service.service_create_new_reimbursement_by_employee_id(reimbursement_with_negative_number)
        assert False
    except NegativeReimbursementException as e:
        assert str(e) == "Reimbursement may not be negative"


def test_invalid_amount_non_numeric_fail():
    try:
        reimbursement_service.service_create_new_reimbursement_by_employee_id(reimbursement_with_non_numeric)
        assert False
    except NonNumericReimbursementAmountException as e:
        assert str(e) == "Reimbursement amount must be an integer"
