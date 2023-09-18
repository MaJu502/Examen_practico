class Departamento:
    def __init__(self, dept_id, nombre, description):
        self.dept_id = dept_id
        self.nombre = nombre
        self.description = description

    def __str__(self):
        return f" >> Department ID: {self.dept_id} with Name: {self.nombre}. Description: {self.description}"

