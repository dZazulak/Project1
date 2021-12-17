from flask import Flask, jsonify, request
from flask_cors import CORS
from custom_exceptions.employee_email_not_found_exception import EmployeeEmailNotFoundException
from custom_exceptions.invalid_email_exception import InvalidEmailException
from custom_exceptions.invalid_password_exception import InvalidPasswordException
from custom_exceptions.manager_email_not_found_exception import ManagerEmailNotFoundException
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDAOImp
from data_access_layer.implementation_classes.manager_dao_imp import ManagerDAOImp
from entities.employee import Employee
from entities.manager import Manager
from service_layer.implementation_services.employee_service_imp import EmployeeServiceImp
import logging

from service_layer.implementation_services.manager_service_imp import ManagerServiceImp

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)
CORS(app)

employee_dao = EmployeeDAOImp()
employee_service = EmployeeServiceImp(employee_dao)
manager_dao = ManagerDAOImp()
manager_service = ManagerServiceImp(manager_dao)


@app.get("/employee/<email>")
def get_employee_information(email: str):
    try:
        result = employee_service.service_get_employee_by_email(email)
        result_as_dictionary = result.make_employee_as_dictionary()
        result_as_json = jsonify(result_as_dictionary)
        return result_as_json

    except EmployeeEmailNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get("/employee")
def get_all_employees_information():
    employees = employee_service.service_get_all_employees()
    employees_as_dictionary = []
    for employee in employees:
        dictionary_employee = employee.make_employee_as_dictionary()
        employees_as_dictionary.append(dictionary_employee)
    return jsonify(employees_as_dictionary)


@app.post("/employee/employeeLogin")
def check_employee_login_information():
    data = request.get_json()
    if data:
        employee_email = data["email"]
        employee_passcode = data["passcode"]
        try:
            return_employee = employee_service.service_check_employee_login(employee_email, employee_passcode)
            employee_as_dictionary = return_employee.make_employee_as_dictionary()
            employee_as_json = jsonify(employee_as_dictionary)
            return employee_as_json
        except InvalidEmailException as e:
            exception_dictionary = {"message": str(e)}
            exception_json = jsonify(exception_dictionary)
            return exception_json
        except InvalidPasswordException as e:
            exception_dictionary = {"message": str(e)}
            exception_json = jsonify(exception_dictionary)
            return exception_json


@app.get("/manager/<manager_id>")
def get_manager_information(email: str):
    try:
        result = manager_service.service_get_manager_by_email(email)
        result_as_dictionary = result.make_manager_as_dictionary()
        result_as_json = jsonify(result_as_dictionary)
        return result_as_json

    except ManagerEmailNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get("/manager")
def get_all_managers_information():
    managers = manager_service.service_get_all_managers()
    managers_as_dictionary = []
    for manager in managers:
        dictionary_manager = manager.make_manager_as_dictionary()
        managers_as_dictionary.append(dictionary_manager)
    return jsonify(managers_as_dictionary)


@app.post("/manager/managerLogin")
def check_manager_login_information():
    data = request.get_json()
    if data:
        manager_email = data["email"]
        manager_passcode = data["passcode"]
        try:
            return_manager = manager_service.service_check_manager_login(manager_email, manager_passcode)
            manager_as_dictionary = return_manager.make_manager_as_dictionary()
            manager_as_json = jsonify(manager_as_dictionary)
            return manager_as_json
        except InvalidEmailException as e:
            exception_dictionary = {"message": str(e)}
            exception_json = jsonify(exception_dictionary)
            return exception_json
        except InvalidPasswordException as e:
            exception_dictionary = {"message": str(e)}
            exception_json = jsonify(exception_dictionary)
            return exception_json


app.run()
