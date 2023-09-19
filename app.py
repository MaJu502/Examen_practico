from backend.backendModel import DataBaseModel
from flask import *

app = Flask(__name__, template_folder='static/templates', static_url_path='/static')
app.config["EXPLAIN_TEMPLATE_LOADING"] = True

model = DataBaseModel()

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/manage_employees', methods=['GET'])
def manage_employees():
    return render_template('manage_employees.html')

@app.route('/manage_departments', methods=['GET'])
def manage_departments():
    return render_template('manage_departments.html')

def obtener_numero_departamento_id(dept):
    return int(dept.dept_id.split('-')[1])

@app.route('/listar_departamentos', methods=['GET'])
def listar_departamentos():
    departamentos = model.listar_departamentos()
    lista_departamentos_ordenados = sorted(departamentos, key=obtener_numero_departamento_id)
    return render_template('listar_departamentos.html', departamentos=lista_departamentos_ordenados)

@app.route('/listar_empleados_departamento', methods=['GET', 'POST'])
def listar_empleados_departamento():
    if request.method == 'POST':
        dept_id = request.form['dept_id']
        # Realiza el query para obtener los empleados del departamento con dept_id
        empleados = model.listar_empleados_departamento(dept_id)  # Asegúrate de tener esta función en tu modelo

        return render_template('listar_empleados_departamento.html', departamentos=empleados)

    # Si la solicitud no es un POST, simplemente muestra la página sin resultados
    return render_template('listar_empleados_departamento.html', departamentos=[])

def obtener_numero_empleado_id(empleado):
    return int(empleado.employee_id.split('-')[1])

@app.route('/listar_empleados', methods=['GET'])
def listar_empleados():
    empleados = model.listar_empleados()
    lista_empleados_ordenados = sorted(empleados, key=obtener_numero_empleado_id)
    return render_template('listar_empleados.html', empleados=lista_empleados_ordenados)

@app.route('/crear_departamento', methods=['POST'])
def crear_departamento():
    if request.method == 'POST':
        dept_id = request.form['dept_id']
        nombre = request.form['nombre']
        description = request.form['description']

        # Verifica si el departamento ya existe
        if model.verif_departamento(dept_id):
            flash("El departamento ya existe.")
            return redirect(url_for("/crear_departamento"))

        resultado = model.crear_departamento(dept_id, nombre, description)
        if resultado is True:
            flash ("Departamento creado con éxito.")
            return redirect(url_for("/crear_departamento"))
        else:
            flash ("Error al crear el departamento: " + resultado)
            return redirect(url_for("/crear_departamento"))
        
@app.route('/crear_empleado', methods=['POST'])
def crear_empleado():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        birthday = request.form['birthday']
        department_id = request.form['department_id']
        employee_id = model.get_next_employee_id()
        

        # Verifica si el empleado ya existe
        if model.verif_empleado(employee_id):
            flash ( "El empleado ya existe.")
            return redirect(url_for("/crear_empleado"))

        resultado = model.crear_empleado(firstname, lastname, birthday, department_id)
        if resultado is True:
            flash ( "Empleado creado con éxito.")
            return redirect(url_for("/crear_empleado"))
        else:
            flash ( "Error al crear el empleado: " + resultado)
            return redirect(url_for("/crear_empleado"))


@app.route('/actualizar_departamento', methods=['GET', 'POST'])
def actualizar_departamento():
    if request.method == 'POST':
        dept_id = request.form['dept_id']
        nombre = request.form['nombre']
        description = request.form['description']
        resultado = model.actualizar_departamento(dept_id, nombre, description)
        if resultado is True:
            flash ( "Departamento actualizado con éxito.")
            return redirect(url_for("/actualizar_departamento"))
        else:
            flash ( "Error al actualizar el departamento: " + resultado)
            return redirect(url_for("/actualizar_departamento"))

@app.route('/actualizar_empleado', methods=['GET', 'POST'])
def actualizar_empleado():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        birthday = request.form['birthday']
        department_id = request.form['department_id']
        resultado = model.actualizar_empleado(employee_id, firstname, lastname, birthday, department_id)
        if resultado is True:
            flash ( "Empleado actualizado con éxito.")
            return redirect(url_for("/actualizar_empleado"))
        else:
            flash ( "Error al actualizar el empleado: " + resultado)
            return redirect(url_for("/actualizar_empleado"))



if __name__ == '__main__':
    app.run(debug=True)