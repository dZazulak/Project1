from data_access_layer.abstract_classes.manager_dao import ManagerDAO
from entities.manager import Manager
from util.database_connection import connection


class ManagerDAOImp(ManagerDAO):

    def get_manager_by_email(self, email: str) -> Manager:
        sql = "select * from project1.manager where email = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [email])
        manager_record = cursor.fetchone()
        manager = Manager(*manager_record)
        return manager

    def get_all_managers(self) -> list[Manager]:
        sql = "select * from project1.manager"
        cursor = connection.cursor()
        cursor.execute(sql)
        manager_records = cursor.fetchall()
        manager_list = []
        for manager in manager_records:
            manager_list.append(Manager(*manager))
        return manager_list

    def check_manager_login(self, email: str, passcode: str):
        sql = "select * from project1.manager where email = %s and passcode = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (email, passcode))
        manager_record = cursor.fetchone()
        manager = Manager(*manager_record)
        return manager
