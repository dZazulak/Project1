from data_access_layer.implementation_classes.manager_dao_imp import ManagerDAOImp
from entities.manager import Manager

manager_dao = ManagerDAOImp()


def test_get_manager_by_email_success():
    returned_manager: Manager = manager_dao.get_manager_by_email("david.zazulak@shield.inc")
    assert returned_manager.manager_id == 2


def test_get_all_managers_success():
    manager_list = manager_dao.get_all_managers()
    assert len(manager_list) >= 2


def test_check_manager_login():
    manager = manager_dao.get_manager_by_email("eric.suminski@shield.inc")
    manager_login = manager_dao.check_manager_login(manager.email, manager.passcode)
    assert (manager_login.manager_id == 1 and manager_login.passcode == "eric")
