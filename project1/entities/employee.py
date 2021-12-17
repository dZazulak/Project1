class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, email: str, passcode: str):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.passcode = passcode

    def make_employee_as_dictionary(self):
        return {
            "employeeID": self.employee_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "passcode": self.passcode
        }

    def __str__(self):
        return "Employee ID: {}, First name: {}, Last name: {}, Email: {}, Passcode: {}".format(self.employee_id, self.first_name, self.last_name, self.email, self.passcode)
