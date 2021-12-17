from data_access_layer.abstract_classes.reimbursement_dao import ReimbursementDAO
from entities.reimbursement import Reimbursement
from util.database_connection import connection


class ReimbursementDAOImp(ReimbursementDAO):

    def get_reimbursement_by_id(self, reimbursement_id: int) -> Reimbursement:
        sql = "select * from project1.reimbursement where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        reimbursement_record = cursor.fetchone()
        reimbursement = Reimbursement(*reimbursement_record)
        return reimbursement

    def get_all_reimbursements_by_id(self) -> list[Reimbursement]:
        sql = "select * from project1.reimbursement"
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_records = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in reimbursement_records:
            reimbursement_list.append(Reimbursement(*reimbursement))
        return reimbursement_list

    def get_all_reimbursements_by_employee_id(self, employee_id: int) -> list[Reimbursement]:
        sql = "select * from project1.reimbursement where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        employee_reimbursement_records = cursor.fetchall()
        employee_reimbursement_list = []
        for employee_reimbursement in employee_reimbursement_records:
            employee_reimbursement_list.append(Reimbursement(*employee_reimbursement))
        return employee_reimbursement_list

    def get_reimbursement_by_approval(self, employee_id: int, approval: str):
        sql = "select * from project1.reimbursement where employee_id = %s and approval = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (employee_id, approval))
        approval_reimbursement_record = cursor.fetchone()
        approval_reimbursement = Reimbursement(*approval_reimbursement_record)
        return approval_reimbursement

    def get_all_reimbursements_by_approval(self, approval: str) -> list[Reimbursement]:
        sql = "select * from project1.reimbursement where approval = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [approval])
        approval_reimbursement_records = cursor.fetchall()
        approval_reimbursement_list = []
        for approval_reimbursement in approval_reimbursement_records:
            approval_reimbursement_list.append(Reimbursement(*approval_reimbursement))
        return approval_reimbursement_list

    def approve_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = "update project1.reimbursement set approval = %s where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.approval, reimbursement.reimbursement_id))
        connection.commit()
        return reimbursement

    def deny_reimbursement(self, reimbursement: Reimbursement):
        sql = "update project1.reimbursement set approval = %s where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.approval, reimbursement.reimbursement_id))
        connection.commit()
        return reimbursement

    def leave_comment_on_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = "update project1.reimbursement set manager_comment = %s where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.manager_comment, reimbursement.reimbursement_id))
        connection.commit()
        return reimbursement

    def get_all_pending_reimbursements_by_manager_id(self, manager_id: int) -> list[Reimbursement]:  # approval: str
        sql = "select * from project1.reimbursement where manager_id = %s and approval = 'Pending'"
        cursor = connection.cursor()
        cursor.execute(sql, [manager_id])
        pending_reimbursement_records = cursor.fetchall()
        pending_reimbursement_list = []
        for pending_reimbursement in pending_reimbursement_records:
            pending_reimbursement_list.append(Reimbursement(*pending_reimbursement))
        return pending_reimbursement_list

    def get_past_reimbursements_by_manager_id(self, manager_id: int, approval: str) -> list[Reimbursement]:
        sql = "select * from project1.reimbursement where manager_id = %s and approval <> 'Pending'"
        cursor = connection.cursor()
        cursor.execute(sql, (manager_id, approval))
        past_reimbursements_records = cursor.fetchall()
        past_reimbursement_list = []
        for past_reimbursement in past_reimbursements_records:
            past_reimbursement_list.append(Reimbursement(*past_reimbursement))
        return past_reimbursement_list

    def view_reimbursement_statistics(self, reimbursement: Reimbursement):
        pass

    def create_new_reimbursement_by_employee_id(self, reimbursement: Reimbursement):
        sql = "insert into project1.reimbursement values(default, %s, %s, %s, %s, %s, %s) returning reimbursement_id"
        cursor = connection.cursor()
        cursor.execute(sql, (
            reimbursement.employee_id, reimbursement.manager_id, reimbursement.amount, reimbursement.approval,
            reimbursement.message, reimbursement.manager_comment))
        connection.commit()
        generated_id = cursor.fetchone()[0]
        reimbursement.reimbursement_id = generated_id
        return reimbursement
