<<<<<<< HEAD
﻿Manual de Usuario Inscriptions App

- **Crea un entorno virtual.**

Para crear un nuevo entorno virtual debemos ejecutar el siguiente comando: 

![](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.001.png)

Para activar debemos ejecutar el siguiente comando si estamos en Windows y nuestra terminal hace uso de PowerShell.

![](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.002.png)

Sabremos que ya estamos en el entorno cuando aparezca el nombre de este a la derecha de la línea de comandos dentro de paréntesis. (.venv)

![](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.003.png)

- **Instalar Django en el entorno virtual.**

Para instalar Django es necesario tener instalado PIP y ejecutar el siguiente comando:

![Texto

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.004.png)

- **Crea un proyecto de Django llamado "InscriptionsApp".** 

Para crear un nuevo proyecto en Django, debemos de ejecutar en la terminal el siguiente comando: 
![](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.005.png)

- **Crea una aplicación dentro del proyecto llamada "Inscriptions".** 

Primero debemos entrar al proyecto con el comando
![](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.006.png)

Para crear la aplicación “Inscriptions” debemos ejecutar el siguiente comando:

![](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.007.png)

Es importante colocar la nueva app dentro de las apps instaladas en el archivo de configuración localizado en “InscriptionsApp/settings.py”

![Texto

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.008.png)

- **Define un modelo "StudentInfo" en el archivo models.py de la aplicación utilizando el tipo de campo que mejor se adecue a la información que será almacenada en este [documento](https://docs.google.com/spreadsheets/d/1MNZ8vjywf5kbJSXP4Gtqjdk9qja65Hra/edit#gid=273215148) .**
  - **Considerar un campo para la fecha de creación del registro y una fecha de actualización de registro.**


Para realizar este paso es necesario acceder al archivo Inscriptions/models.py y definir el modelo como se muestra a continuación

![Texto

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.009.png)

- **Ejecuta las migraciones para crear la tabla en la base de datos.** 

**Para realizar este paso, es necesario ejecutar los siguientes comandos:
![Texto

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.010.png)**

- **Crea tres registros utilizando el administrador de Django.** 


Para utilizar el administrador de Djando, primero debemos crear un super usuario con el siguiente comando:
![Texto

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.011.png)

En este caso nos resulta un warning ya que tanto el user como el password es **admin** 

**username: admin
password : admin**

Ahora debemos registrar el modelo en el archivo **admin.py (Inscriptions/admin.py)**   Como se muestra a continuación:
![Texto

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.012.png)
=======
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
 
>>>>>>> d433447ca403991bc7ff645330046a861430eda3

Ahora ya podemos iniciar el servidor con el siguiente comando


Una vez iniciado el servidor accedemos a 127.0.0.1:8000/admin nos logueamos con las credenciales que creamos anteriormente en la línea de comandos y así podremos acceder al panel de administración 
<<<<<<< HEAD

![Interfaz de usuario gráfica, Aplicación, Sitio web

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.013.png)
Creamos el usuario **fer\_gallegos** con su contraseña **admin1..**  y el usuario **manuel\_juarez** con el password **manu1..@**


![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.014.png)

![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.015.png)

Creamos el grupo 1
![Interfaz de usuario gráfica, Texto, Aplicación

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.016.png)

- **Define una vista llamada "student\_list" en el archivo views.py de la aplicación "Inscriptions" que muestre todos los posts ordenados por fecha de creación descendente.** 

Para ello es necesario modificar el archivo views.py que se encuentra dentro de “Inscriptions/views.py” 

![Texto

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.017.png)

- **Crea una URL para la vista "student\_list" en el archivo urls.py de la aplicación "Inscriptions" y asegúrate de que sea la página principal del proyecto.** 

Para realizar este paso es necesario crear el archivo “Inscriptions/urls.py” y configurar la url como se muestra a continuación:

![](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.018.png)

Ahora debemos modificar el archivo “InscriptionsApp/urls.py” para incluir las url de la aplicación, quedando de la siguiente manera: 

![Texto

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.019.png)

- **Renderiza la información de los estudiantes (Nombre,apellido,correo y matricula) en una plantilla HTML llamada "student\_list.html" utilizando un bucle for.** 

Para realizar este paso es necesario crear una plantilla html en el directorio “Inscriptions/templates” y nombrarlo “student\_list.html” con el siguiente contenido:

![Texto

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.020.png)



La vista principal luce de esta manera:
![Interfaz de usuario gráfica, Texto, Aplicación

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.021.png)

- Utiliza el ORM de Django para realizar las siguientes querys y separar por secciones el resultado :
  - Obtener el número total de estudiantes en la vista "student\_list" y muéstralo en la plantilla. 
    - Ejemplo: Cantidad de estudiantes : 20
  - **Filtrar por estudiantes que tengan fecha de inicio y formatear la fecha a formato (dd-mm-yyyy) y mostrarla matrícula junto a la fecha de inicio.**
    - **Ejemplo: 400000111- 14-01-2023**


      La vista con filtro de fecha\_inicio luce así, es una vista dinámica que se irá adaptando a los filtros:
      ![Interfaz de usuario gráfica, Texto, Aplicación

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.022.png)
  - Filtrar y separar los alumnos por género masculino y femenino en dos columnas diferentes.
    - Ejemplo: 400000111-Masculino

      ![Interfaz de usuario gráfica, Aplicación

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.023.png)
  - Filtrar por tipo de moneda del alumno, mostrar en 3 columnas diferentes  y mostrar la matrícula junto a la moneda.
    - Ejemplo: 400000111-MXN

      ![Interfaz de usuario gráfica, Texto, Aplicación, Correo electrónico

Descripción generada automáticamente](Aspose.Words.69b2129a-a0b8-4ab8-9a56-6188bc84053f.024.png)

Puedes utilizar cualquier versión de Django compatible con tu entorno de desarrollo. 
=======
 
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
>>>>>>> d433447ca403991bc7ff645330046a861430eda3

