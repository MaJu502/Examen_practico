# Escenario de análisis
Para contemplar la funcionalidad de manejo de asistencia de empleados en el sistema hay que realizar cambios primeramente en la base de datos para tener así la información de asistencias. Para esto se debería de considerar una tabla adicional en la base de datos SQL con la intencion de no sobrecargar y tener más facil y rápido acceso a la tabla de empleados. Esto principalmente pues si añadimos la asistencia a la ya existente tabla de Empleados estariamos generando mucha redundancia y duplicados en los registros y sería relativamente más complicado y lento realizar consultas que se necesitan de manera rápida. Por esto se propone la tabla de Asistencia donde se tendría la siguiente información:

- asis_date_in: Date
- asis_date_out: Date
- asis_type: Text
- (FK1) employee_id: Text

Con esto se logra ligar la tabla de Asistencia a la tabla de Empleados mediante la llave foreign employee_id. Así mismo se deberia de considerar las posibles razones o motivos para una ausencia al trabajo y algo importante es considerar la información de un **asis_type** ya sea por:
- vacaciones
- enfermedad
- presente
- ausente
- tarde

esto permite llevar control de los días de vacaciones, días de licencia por enfermedad y saber y tener respaldo de toda la información por alguna situación legal con los empleados. 

### Posible caso/solución

Se debe de determinar si la misma funcionalidad será automatizada o realizada manualmente por un operario/usuario. Si esta fuera automatizada se deberia de tener un sistema que determine las llamadas telefónicas y pueda así ingresar la asistencia del Empleado en el sistema una vez el mismo acepte la llamada. Por otro lado de ser ingresada manualmente por un usuario se debe de agregar las funcionalidades y respectivas vistas en el programa para permitir los siguientes casos de uso:
- Ingresar asistencia
- Modificar asistencia
- Ver días de vacaciones de un empleado X
- Ver días de licencia por enfermedad de un empleado X
- Ver días ausente de un empleado X
- Ver días  de llegar tarde de un empleado X

Estas funcionalidades se pueden agrupar en una sola vista de manejo de asistencia en la cual se debe de permitir hacer primordialmente el ingreso de una asistencia de manera rápida y muy intuitiva para que la tarea de realizar dicha actividad en el sistema web no sea complicada ya que será algo realizado a diario muchas veces.


### Otro posible caso/solución
Se debe de considerar el inicio de sesión en un programa ya sea distinto a este o este mismo para poder permitir a los usuarios ingresar su hora de llegada a su área. Este debería ya sea ser de monitorio para permitir monitorear el sistema donde trabajan los empleados y realizarlo de manera automática con la intención de que esto mismo funcione en "backend" todo el tiempo.