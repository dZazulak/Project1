class Reimbursement:
    def __init__(self, reimbursement_id: int, employee_id: int, manager_id: int, amount: float,
                 approval: str, message: str, manager_comment: str):
        self.reimbursement_id = reimbursement_id
        self.employee_id = employee_id
        self.manager_id = manager_id
        self.amount = amount
        self.approval = approval
        self.message = message
        self.manager_comment = manager_comment

    def make_reimbursement_as_dictionary(self):
        return {
            "reimbursementID": self.reimbursement_id,
            "employeeID": self.employee_id,
            "managerID": self.manager_id,
            "amount": self.amount,
            "approval": self.approval,
            "message": self.message,
            "managerComment": self.manager_comment
        }

    def __str__(self):
        return "ReimbursementID: {}, EmployeeID: {}, ManagerID: {}, Amount: {}, Approval: {}, Message: {}, " \
               "ManagerComment: {}".format(self.reimbursement_id, self.employee_id, self.manager_id, self.amount,
                                           self.approval, self.message, self.manager_comment)
