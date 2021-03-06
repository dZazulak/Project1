from abc import ABC, abstractmethod
from entities.reimbursement import Reimbursement


class ReimbursementService(ABC):

    @abstractmethod
    def service_get_reimbursement_by_id(self, reimbursement_id: int) -> Reimbursement:
        pass

    @abstractmethod
    def service_get_all_reimbursements_by_id(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_get_all_reimbursements_by_employee_id(self, employee_id: int) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_approve_reimbursement(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def service_deny_reimbursement(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def service_get_all_pending_reimbursements_by_manager_id(self, manager_id: int) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_get_past_reimbursements_by_manager_id(self, manager_id: int) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_create_new_reimbursement_by_employee_id(self, reimbursement: Reimbursement):
        pass

    @abstractmethod
    def service_get_all_employee_reimbursement_statistics(self, employee_id: int):
        pass
