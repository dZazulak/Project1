from custom_exceptions.login_failed_exception import LoginFailedException
from data_access_layer.abstract_classes.employee_dao import EmployeeDAO
from entities.employee import Employee
from util.database_connection import connection


class EmployeeDAOImp(EmployeeDAO):

    def get_employee_by_email(self, email: str) -> Employee:
        sql = "select * from project1.employee where email = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [email])
        employee_record = cursor.fetchone()
        employee = Employee(*employee_record)
        return employee

    def get_all_employees(self) -> list[Employee]:
        sql = "select * from project1.employee"
        cursor = connection.cursor()
        cursor.execute(sql)
        employee_records = cursor.fetchall()
        employee_list = []
        for employee in employee_records:
            employee_list.append(Employee(*employee))
        return employee_list

    def check_employee_login(self, email: str, passcode: str) -> Employee:
        sql = "select * from project1.employee where email = %s and passcode = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (email, passcode))
        employee_record = cursor.fetchone()
        employee = Employee(*employee_record)
        return employee

