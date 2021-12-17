from abc import ABC, abstractmethod
from entities.manager import Manager


class ManagerService(ABC):

    @abstractmethod
    def service_get_manager_by_email(self, email: str) -> Manager:
        pass

    @abstractmethod
    def service_get_all_managers(self) -> list[Manager]:
        pass

    @abstractmethod
    def service_check_manager_login(self, email: str, passcode: str):
        pass
