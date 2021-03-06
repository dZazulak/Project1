from abc import ABC, abstractmethod
from entities.reimbursement import Reimbursement


class ReimbursementDAO(ABC):

    @abstractmethod
    def get_reimbursement_by_id(self, reimbursement_id: int) -> Reimbursement:
        pass

    @abstractmethod
    def get_all_reimbursements_by_id(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def get_all_reimbursements_by_employee_id(self, employee_id: int) -> list[Reimbursement]:
        pass

    @abstractmethod
    def approve_reimbursement(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def deny_reimbursement(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def get_all_pending_reimbursements_by_manager_id(self, manager_id: int) -> list[Reimbursement]:
        pass

    @abstractmethod
    def get_past_reimbursements_by_manager_id(self, manager_id: int) -> list[Reimbursement]:
        pass

    @abstractmethod
    def create_new_reimbursement_by_employee_id(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def get_all_employee_reimbursement_statistics(self, employee_id: int):
        pass

