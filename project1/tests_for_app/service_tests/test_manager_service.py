from custom_exceptions.invalid_email_exception import InvalidEmailException
from custom_exceptions.invalid_password_exception import InvalidPasswordException
from custom_exceptions.manager_email_not_found_exception import ManagerEmailNotFoundException
from data_access_layer.implementation_classes.manager_dao_imp import ManagerDAOImp
from entities.manager import Manager
from service_layer.implementation_services.manager_service_imp import ManagerServiceImp

manager_dao = ManagerDAOImp()
manager_service = ManagerServiceImp(manager_dao)


def test_get_manager_id_fail():
    try:
        manager_service.service_get_manager_by_email("dave")
        assert False
    except ManagerEmailNotFoundException as e:
        assert str(e) == "Manager email was not found."


def test_check_manager_login_email_fail():
    try:
        manager_service.service_check_manager_login("dave.zazulak@shield.inc", "david")
        assert False
    except InvalidEmailException as e:
        assert str(e) == "Invalid email"


def test_check_manager_login_password_fail():
    try:
        manager_service.service_check_manager_login("eric.suminski@shield.inc", "ericcc")
        assert False
    except InvalidPasswordException as e:
        assert str(e) == "Invalid password"
