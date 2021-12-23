from custom_exceptions.duplicate_reimbursement_id_exception import DuplicateReimbursementIdException
from custom_exceptions.employee_id_not_found_exception import EmployeeIdNotFoundException
from custom_exceptions.invalid_approval_statement_exception import InvalidApprovalStatementException
from custom_exceptions.manager_id_not_found_exception import ManagerIdNotFoundException
from custom_exceptions.negative_reimbursement_exception import NegativeReimbursementException
from custom_exceptions.non_numeric_reimbursement_amount_exception import NonNumericReimbursementAmountException
from custom_exceptions.reimbursement_not_found_exception import ReimbursementNotFoundException
from custom_exceptions.too_many_characters_in_comment_exception import TooManyCharactersInCommentException
from service_layer.abstract_services.reimbursement_service import ReimbursementService
from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAO
from entities.reimbursement import Reimbursement


class ReimbursementServiceImp(ReimbursementService):
    def __init__(self, reimbursement_dao: ReimbursementDAO):
        self.reimbursement_dao = reimbursement_dao

    def service_get_reimbursement_by_id(self, reimbursement_id: int) -> Reimbursement:
        reimbursement_list = self.reimbursement_dao.get_all_reimbursements_by_id()
        for existing_reimbursement in reimbursement_list:
            if existing_reimbursement.reimbursement_id == reimbursement_id:
                return self.reimbursement_dao.get_reimbursement_by_id(reimbursement_id)
        raise ReimbursementNotFoundException("Reimbursement ID was not found")

    def service_get_all_reimbursements_by_id(self) -> list[Reimbursement]:
        return self.reimbursement_dao.get_all_reimbursements_by_id()

    def service_get_all_reimbursements_by_employee_id(self, employee_id: int) -> list[Reimbursement]:
        reimbursement_list = self.reimbursement_dao.get_all_reimbursements_by_id()
        for existing_reimbursement in reimbursement_list:
            if existing_reimbursement.employee_id == employee_id:
                return self.reimbursement_dao.get_all_reimbursements_by_employee_id(employee_id)
        raise EmployeeIdNotFoundException("Employee ID was not found")

    def service_approve_reimbursement(self, reimbursement: Reimbursement):
        reimbursement_list = self.reimbursement_dao.get_all_reimbursements_by_id()
        for existing_reimbursements in reimbursement_list:
            if existing_reimbursements.reimbursement_id == reimbursement.reimbursement_id:
                if existing_reimbursements.manager_id == reimbursement.manager_id:
                    if existing_reimbursements.employee_id == reimbursement.employee_id:
                        if reimbursement.approval == "Approved":
                            if len(reimbursement.manager_comment) <= 200:
                                return self.reimbursement_dao.approve_reimbursement(reimbursement)
                            raise TooManyCharactersInCommentException("Too many characters in the comment")
                        raise InvalidApprovalStatementException("Invalid approval")
                    raise EmployeeIdNotFoundException("Employee ID was not found")
                raise ManagerIdNotFoundException("Manager ID was not found")

    def service_deny_reimbursement(self, reimbursement: Reimbursement):
        reimbursement_list = self.reimbursement_dao.get_all_reimbursements_by_id()
        for existing_reimbursements in reimbursement_list:
            if existing_reimbursements.reimbursement_id == reimbursement.reimbursement_id:
                if existing_reimbursements.manager_id == reimbursement.manager_id:
                    if existing_reimbursements.employee_id == reimbursement.employee_id:
                        if reimbursement.approval == "Denied":
                            if len(reimbursement.manager_comment) <= 200:
                                return self.reimbursement_dao.approve_reimbursement(reimbursement)
                            raise TooManyCharactersInCommentException("Too many characters in the comment")
                        raise InvalidApprovalStatementException("Invalid approval")
                    raise EmployeeIdNotFoundException("Employee ID was not found")
                raise ManagerIdNotFoundException("Manager ID was not found")

    def service_get_all_pending_reimbursements_by_manager_id(self, manager_id: int) -> list[Reimbursement]:
        reimbursement_list = self.reimbursement_dao.get_all_reimbursements_by_id()
        for existing_reimbursements in reimbursement_list:
            if existing_reimbursements.manager_id == manager_id:
                if existing_reimbursements.approval == "Pending":
                    return self.reimbursement_dao.get_all_pending_reimbursements_by_manager_id(manager_id)
        raise ManagerIdNotFoundException("Manager ID was not found")

    def service_get_past_reimbursements_by_manager_id(self, manager_id: int) -> list[Reimbursement]:
        reimbursement_list = self.reimbursement_dao.get_all_reimbursements_by_id()
        for existing_reimbursements in reimbursement_list:
            if existing_reimbursements.manager_id == manager_id:
                if existing_reimbursements.approval != "Pending":
                    return self.reimbursement_dao.get_past_reimbursements_by_manager_id(manager_id)
        raise ManagerIdNotFoundException("Manager ID was not found")

    def service_create_new_reimbursement_by_employee_id(self, reimbursement: Reimbursement):
        if reimbursement.approval == "Pending":
            if type(reimbursement.amount) == int:
                if reimbursement.amount > 0:
                    return self.reimbursement_dao.create_new_reimbursement_by_employee_id(reimbursement)
                raise NegativeReimbursementException("Reimbursement may not be negative")
            raise NonNumericReimbursementAmountException("Reimbursement amount must be an integer")
        raise InvalidApprovalStatementException("Invalid approval")

    def service_get_all_employee_reimbursement_statistics(self, employee_id: int):
        reimbursement_list = self.reimbursement_dao.get_all_reimbursements_by_employee_id(employee_id)
        for existing_reimbursements in reimbursement_list:
            if existing_reimbursements.employee_id == employee_id:
                return self.reimbursement_dao.get_all_employee_reimbursement_statistics(employee_id)
            raise EmployeeIdNotFoundException("Employee ID was not found")
