# InscriptionsApp
InscriptionsApp is a trial application which simulates being a small school siu system


Manual de Usuario Inscriptions App

•	Crea un entorno virtual.
Para crear un nuevo entorno virtual debemos ejecutar el siguiente comando: 
 
Para activar debemos ejecutar el siguiente comando si estamos en Windows y nuestra terminal hace uso de PowerShell.
 
Sabremos que ya estamos en el entorno cuando aparezca el nombre de este a la derecha de la línea de comandos dentro de paréntesis. (.venv)
 

•	Instalar Django en el entorno virtual.
Para instalar Django es necesario tener instalado PIP y ejecutar el siguiente comando:
 
•	Crea un proyecto de Django llamado "InscriptionsApp". 
Para crear un nuevo proyecto en Django, debemos de ejecutar en la terminal el siguiente comando: 
 


•	Crea una aplicación dentro del proyecto llamada "Inscriptions". 

Primero debemos entrar al proyecto con el comando
 
Para crear la aplicación “Inscriptions” debemos ejecutar el siguiente comando:
 

Es importante colocar la nueva app dentro de las apps instaladas en el archivo de configuración localizado en “InscriptionsApp/settings.py”

 

•	Define un modelo "StudentInfo" en el archivo models.py de la aplicación utilizando el tipo de campo que mejor se adecue a la información que será almacenada en este documento .
•	Considerar un campo para la fecha de creación del registro y una fecha de actualización de registro.

Para realizar este paso es necesario acceder al archivo Inscriptions/models.py y definir el modelo como se muestra a continuación

 

•	Ejecuta las migraciones para crear la tabla en la base de datos. 

Para realizar este paso, es necesario ejecutar los siguientes comandos:
 

•	Crea tres registros utilizando el administrador de Django. 

Para utilizar el administrador de Djando, primero debemos crear un super usuario con el siguiente comando:
 

En este caso nos resulta un warning ya que tanto el user como el password es admin 

username: admin
password : admin

Ahora debemos registrar el modelo en el archivo admin.py (Inscriptions/admin.py)   Como se muestra a continuación:
 

Ahora ya podemos iniciar el servidor con el siguiente comando


Una vez iniciado el servidor accedemos a 127.0.0.1:8000/admin nos logueamos con las credenciales que creamos anteriormente en la línea de comandos y así podremos acceder al panel de administración 
 
Creamos el usuario fer_gallegos con su contraseña admin1..  y el usuario manuel_juarez con el password manu1..@

 
 
Creamos el grupo 1
 

•	Define una vista llamada "student_list" en el archivo views.py de la aplicación "Inscriptions" que muestre todos los posts ordenados por fecha de creación descendente. 

Para ello es necesario modificar el archivo views.py que se encuentra dentro de “Inscriptions/views.py” 
 

•	Crea una URL para la vista "student_list" en el archivo urls.py de la aplicación "Inscriptions" y asegúrate de que sea la página principal del proyecto. 

Para realizar este paso es necesario crear el archivo “Inscriptions/urls.py” y configurar la url como se muestra a continuación:
 

Ahora debemos modificar el archivo “InscriptionsApp/urls.py” para incluir las url de la aplicación, quedando de la siguiente manera: 

 


•	Renderiza la información de los estudiantes (Nombre,apellido,correo y matricula) en una plantilla HTML llamada "student_list.html" utilizando un bucle for. 

Para realizar este paso es necesario crear una plantilla html en el directorio “Inscriptions/templates” y nombrarlo “student_list.html” con el siguiente contenido:
 


La vista principal luce de esta manera:
 

•	Utiliza el ORM de Django para realizar las siguientes querys y separar por secciones el resultado :
•	Obtener el número total de estudiantes en la vista "student_list" y muéstralo en la plantilla. 
•	Ejemplo: Cantidad de estudiantes : 20
•	Filtrar por estudiantes que tengan fecha de inicio y formatear la fecha a formato (dd-mm-yyyy) y mostrarla matrícula junto a la fecha de inicio.
•	Ejemplo: 400000111- 14-01-2023


La vista con filtro de fecha_inicio luce así, es una vista dinámica que se irá adaptando a los filtros:
 


•	Filtrar y separar los alumnos por género masculino y femenino en dos columnas diferentes.
•	Ejemplo: 400000111-Masculino

 
•	Filtrar por tipo de moneda del alumno, mostrar en 3 columnas diferentes  y mostrar la matrícula junto a la moneda.
•	Ejemplo: 400000111-MXN

 
Puedes utilizar cualquier versión de Django compatible con tu entorno de desarrollo. 

