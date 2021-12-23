from flask import Flask, jsonify, request
from flask_cors import CORS
from custom_exceptions.employee_email_not_found_exception import EmployeeEmailNotFoundException
from custom_exceptions.employee_id_not_found_exception import EmployeeIdNotFoundException
from custom_exceptions.invalid_approval_statement_exception import InvalidApprovalStatementException
from custom_exceptions.invalid_email_exception import InvalidEmailException
from custom_exceptions.invalid_password_exception import InvalidPasswordException
from custom_exceptions.manager_email_not_found_exception import ManagerEmailNotFoundException
from custom_exceptions.manager_id_not_found_exception import ManagerIdNotFoundException
from custom_exceptions.negative_reimbursement_exception import NegativeReimbursementException
from custom_exceptions.non_numeric_reimbursement_amount_exception import NonNumericReimbursementAmountException
from custom_exceptions.reimbursement_not_found_exception import ReimbursementNotFoundException
from data_access_layer.implementation_classes.employee_dao_imp import EmployeeDAOImp
from data_access_layer.implementation_classes.manager_dao_imp import ManagerDAOImp
from data_access_layer.implementation_classes.reimbursement_dao_imp import ReimbursementDAOImp
from service_layer.implementation_services.employee_service_imp import EmployeeServiceImp
import logging
from service_layer.implementation_services.manager_service_imp import ManagerServiceImp
from service_layer.implementation_services.reimbursement_service_imp import ReimbursementServiceImp
from entities.employee import Employee
from entities.manager import Manager
from entities.reimbursement import Reimbursement

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)
CORS(app)

employee_dao = EmployeeDAOImp()
employee_service = EmployeeServiceImp(employee_dao)
manager_dao = ManagerDAOImp()
manager_service = ManagerServiceImp(manager_dao)
reimbursement_dao = ReimbursementDAOImp()
reimbursement_service = ReimbursementServiceImp(reimbursement_dao)


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


@app.get("/manager/<email>")
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


@app.get("/reimbursement/<reimbursement_id>")
def get_reimbursement_information_by_id(reimbursement_id: int):
    try:
        result = reimbursement_service.service_get_reimbursement_by_id(int(reimbursement_id))
        result_as_dictionary = result.make_reimbursement_as_dictionary()
        result_as_json = jsonify(result_as_dictionary)
        return result_as_json
    except ReimbursementNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get("/reimbursement")
def get_all_reimbursements_by_id():
    reimbursements = reimbursement_service.service_get_all_reimbursements_by_id()
    reimbursements_as_dictionary = []
    for reimbursement in reimbursements:
        dictionary_reimbursement = reimbursement.make_reimbursement_as_dictionary()
        reimbursements_as_dictionary.append(dictionary_reimbursement)
    return jsonify(reimbursements_as_dictionary)


@app.get("/employee/<employee_id>/reimbursements")
def get_all_reimbursements_by_employee_id(employee_id: int):
    try:
        reimbursements = reimbursement_service.service_get_all_reimbursements_by_employee_id(int(employee_id))
        reimbursements_as_dictionary = []
        for reimbursement in reimbursements:
            dictionary_reimbursement = reimbursement.make_reimbursement_as_dictionary()
            reimbursements_as_dictionary.append(dictionary_reimbursement)
        return jsonify(reimbursements_as_dictionary)
    except EmployeeIdNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get("/manager/<manager_id>/pending_reimbursements")
def get_all_pending_reimbursements_by_manager_id(manager_id: int):
    try:
        reimbursements = reimbursement_service.service_get_all_pending_reimbursements_by_manager_id(int(manager_id))
        reimbursements_as_dictionary = []
        for reimbursement in reimbursements:
            dictionary_reimbursement = reimbursement.make_reimbursement_as_dictionary()
            reimbursements_as_dictionary.append(dictionary_reimbursement)
        return jsonify(reimbursements_as_dictionary)
    except ManagerIdNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get("/manager/<manager_id>/past_reimbursements")
def get_all_past_reimbursements_by_manager_id(manager_id: int):
    try:
        reimbursements = reimbursement_service.service_get_past_reimbursements_by_manager_id(int(manager_id))
        reimbursements_as_dictionary = []
        for reimbursement in reimbursements:
            dictionary_reimbursement = reimbursement.make_reimbursement_as_dictionary()
            reimbursements_as_dictionary.append(dictionary_reimbursement)
        return jsonify(reimbursements_as_dictionary)
    except ManagerIdNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.post("/new_reimbursement")
def create_new_reimbursement_by_employee_id():
    try:
        reimbursement_data = request.get_json()
        new_reimbursement = Reimbursement(
            reimbursement_data["reimbursementId"],
            reimbursement_data["employeeId"],
            reimbursement_data["managerId"],
            reimbursement_data["amount"],
            reimbursement_data["approval"],
            reimbursement_data["message"],
            reimbursement_data["managerComment"]
        )
        reimbursement_to_return = reimbursement_service.service_create_new_reimbursement_by_employee_id(
            new_reimbursement)
        reimbursement_as_dictionary = reimbursement_to_return.make_reimbursement_as_dictionary()
        reimbursement_as_json = jsonify(reimbursement_as_dictionary)
        return reimbursement_as_json
    except NegativeReimbursementException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except NonNumericReimbursementAmountException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except InvalidApprovalStatementException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.patch("/reimbursement/approve/<reimbursement_id>")
def approve_reimbursement(reimbursement_id: int):
    try:
        reimbursement_data = request.get_json()
        approved_reimbursement = Reimbursement(
            int(reimbursement_id),
            reimbursement_data["employeeId"],
            reimbursement_data["managerId"],
            reimbursement_data["amount"],
            reimbursement_data["approval"],
            reimbursement_data["message"],
            reimbursement_data["managerComment"]
        )
        updated_reimbursement = reimbursement_service.service_approve_reimbursement(approved_reimbursement)
        updated_reimbursement_as_dictionary = updated_reimbursement.make_reimbursement_as_dictionary()
        return jsonify(updated_reimbursement_as_dictionary)
    except ManagerIdNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except ReimbursementNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except EmployeeIdNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except InvalidApprovalStatementException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.patch("/reimbursement/deny/<reimbursement_id>")
def deny_reimbursement(reimbursement_id: int):
    try:
        reimbursement_data = request.get_json()
        denied_reimbursement = Reimbursement(
            int(reimbursement_id),
            reimbursement_data["employeeId"],
            reimbursement_data["managerId"],
            reimbursement_data["amount"],
            reimbursement_data["approval"],
            reimbursement_data["message"],
            reimbursement_data["managerComment"]
        )
        updated_reimbursement = reimbursement_service.service_deny_reimbursement(denied_reimbursement)
        updated_reimbursement_as_dictionary = updated_reimbursement.make_reimbursement_as_dictionary()
        return jsonify(updated_reimbursement_as_dictionary)
    except ManagerIdNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except ReimbursementNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except EmployeeIdNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except InvalidApprovalStatementException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get("/employee/statistics/<employee_id>")
def sum_employee_reimbursements(employee_id: int):
    try:
        employee_reimbursement_statistics = reimbursement_service.service_get_all_employee_reimbursement_statistics(
            int(employee_id))
        return jsonify(employee_reimbursement_statistics)

    except EmployeeIdNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


app.run()
