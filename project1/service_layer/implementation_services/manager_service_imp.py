from custom_exceptions.invalid_email_exception import InvalidEmailException
from custom_exceptions.invalid_password_exception import InvalidPasswordException
from custom_exceptions.manager_email_not_found_exception import ManagerEmailNotFoundException
from data_access_layer.implementation_classes.manager_dao_imp import ManagerDAO
from entities.manager import Manager
from service_layer.abstract_services.manager_service import ManagerService


class ManagerServiceImp(ManagerService):
    def __init__(self, manager_dao: ManagerDAO):
        self.manager_dao = manager_dao

    def service_get_manager_by_email(self, email: str) -> Manager:
        manager_list = self.manager_dao.get_all_managers()
        for current_manager in manager_list:
            if current_manager.email == email:
                return self.manager_dao.get_manager_by_email(email)
        raise ManagerEmailNotFoundException("Manager email was not found.")

    def service_get_all_managers(self) -> list[Manager]:
        return self.manager_dao.get_all_managers()

    def service_check_manager_login(self, email: str, passcode: str):
        manager_list = self.manager_dao.get_all_managers()
        for current_manager in manager_list:
            if current_manager.email == email:
                if current_manager.passcode == passcode:
                    return self.manager_dao.check_manager_login(email, passcode)
                raise InvalidPasswordException("Invalid password")
        raise InvalidEmailException("Invalid email")

