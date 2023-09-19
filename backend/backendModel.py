import psycopg2
from backend.empleado import Empleado
from backend.departamento import Departamento

class DataBaseModel:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="eujtungq",
            user="eujtungq",
            password="ybkaeOQyGHFBAw9lE1m6kj5CvH3euM_n",
            host="mahmud.db.elephantsql.com",
            port="5432"
        )
        self.conn.autocommit = (True)
        self.cursor = self.conn.cursor()

    def listar_departamentos(self):
        self.cursor.execute("SELECT * FROM Departamento")
        departamentos = []
        for row in self.cursor.fetchall():
            dept_id, nombre, description = row
            departamento = Departamento(dept_id, nombre, description)
            departamentos.append(departamento)
        return departamentos

    def listar_empleados(self):
        self.cursor.execute("SELECT * FROM Empleado")
        empleados = []
        for row in self.cursor.fetchall():
            employee_id, firstname, lastname, birthday, department_id = row
            empleado = Empleado(employee_id, firstname, lastname, birthday, department_id)
            empleados.append(empleado)
        return empleados
    
    def listar_empleados_departamento(self,dep):
        dep = dep.replace(" ", "")
        self.cursor.execute("SELECT * FROM Empleado WHERE department_id LIKE '{}'".format(dep))
        empleados = []
        for row in self.cursor.fetchall():
            print('-->',row)
            employee_id, firstname, lastname, birthday, department_id = row
            empleado = Empleado(employee_id, firstname, lastname, birthday, department_id)
            empleados.append(empleado)
        return empleados

    def crear_departamento(self, dept_id, nombre, description):
        try:
            self.cursor.execute("INSERT INTO Departamento (dept_id, nombre, description) VALUES (%s, %s, %s)", (dept_id, nombre, description))
            return True
        except Exception as e:
            return str(e)

    def crear_empleado(self, firstname, lastname, birthday, department_id):
        try:
            self.cursor.execute("INSERT INTO Empleado (firstname, lastname, birthday, department_id) VALUES (%s, %s, %s, %s)", (firstname, lastname, birthday, department_id))
            return True
        except Exception as e:
            return str(e)

    def actualizar_departamento(self, dept_id, nombre, description):
        try:
            self.cursor.execute("UPDATE Departamento SET nombre = %s, description = %s WHERE dept_id = %s", (nombre, description, dept_id))
            return True
        except Exception as e:
            return str(e)

    def actualizar_empleado(self, employee_id, firstname, lastname, birthday, department_id):
        try:
            self.cursor.execute("UPDATE Empleado SET firstname = %s, lastname = %s, birthday = %s, department_id = %s WHERE employee_id = %s", (firstname, lastname, birthday, department_id, employee_id))
            return True
        except Exception as e:
            return str(e)

    def eliminar_departamento(self, dept_id):
        try:
            self.cursor.execute("DELETE FROM Departamento WHERE dept_id = %s", (dept_id,))
            return True
        except Exception as e:
            return str(e)

    def eliminar_empleado(self, employee_id):
        try:
            self.cursor.execute("DELETE FROM Empleado WHERE employee_id = %s", (employee_id,))
            return True
        except Exception as e:
            return str(e)
        
    def verif_empleado(self, employee_id):
        try:
            self.cursor.execute("SELECT * FROM Empleado WHERE employee_id = %s", (employee_id,))
            return True
        except Exception as e:
            return str(e)
        
    def verif_departamento(self, dept_id):
        try:
            self.cursor.execute("SELECT * FROM Departamento WHERE dept_id = %s", (dept_id,))
            return True
        except Exception as e:
            return str(e)
        
    def get_next_employee_id(self):
        try:
            self.cursor.execute("SELECT MAX(employee_id) AS ultimo_id_agregado FROM Empleado;")
            result = self.cursor.fetchone()
            if result and result[0]:
                ultimo_id = result[0]
                ultimo_numero = int(ultimo_id.split('-')[1])
                nuevo_numero = ultimo_numero + 1
                nuevo_employee_id = f"EMP-{nuevo_numero:04d}"
                return nuevo_employee_id
            else:
                # Si no hay registros en la tabla Empleado, comienza desde EMP-0001
                return "EMP-0001"
        except Exception as e:
            return str(e)

