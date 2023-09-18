class Empleado:
    def __init__(self, employee_id, firstname, lastname, department_id, birthday=None):
        self.employee_id = employee_id
        self.firstname = firstname
        self.lastname = lastname
        self.department_id = department_id
        self.birthday = birthday

    def __str__(self):
        return f" >> Employee {self.firstname} {self.lastname} with Employee ID: {self.employee_id} from Department ID: {self.department_id}"
