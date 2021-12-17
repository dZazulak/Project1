class Manager:
    def __init__(self, manager_id: int, first_name: str, last_name: str, email: str, passcode: str):
        self.manager_id = manager_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.passcode = passcode

    def make_manager_as_dictionary(self):
        return {
            "managerID": self.manager_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "passcode": self.passcode
        }

    def __str__(self):
        return "Manager ID: {}, First name: {}, Last name: {}, Email: {}, Passcode: {}".format(self.manager_id,
                                                                                               self.first_name,
                                                                                               self.last_name,
                                                                                               self.email,
                                                                                               self.passcode)
