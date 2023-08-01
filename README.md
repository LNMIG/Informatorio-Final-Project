# Informatorio-Final-Project
Proyecto final de la segunda etapa del Informatorio 2023 usando Python, Django, HTML, CSS, MySQL y deployado en pythonanywhere.


## Página de Inicio
* Un usuario no registrado verá que puede loguearse, registrarse y navegar.
![2023-07-31 (3)](https://github.com/LNMIG/Informatorio_Final_Project/assets/96741070/dbde0c80-51ea-4f72-9bec-44d547bf45c0)


## Filtrado de posts por Categorías
* Un usuario no registrado o registrado podrá filtrar los posts por categorías.
![2023-07-31 (4)](https://github.com/LNMIG/Informatorio_Final_Project/assets/96741070/b1c33687-79d3-40a5-b905-aab76a790a87)


## Filtrado de posts por fecha de publicación
* Un usuario no registrado o registrado podrá filtrar los posts por fecha de creación.
![2023-07-31 (5)](https://github.com/LNMIG/Informatorio_Final_Project/assets/96741070/1c6274da-e19e-4f37-9f09-7e0d314f1042)


## Página de Registro
![2023-07-31 (6)](https://github.com/LNMIG/Informatorio_Final_Project/assets/96741070/a2a64de4-4a6a-40ef-a45d-5144ab340780)


## Página para Loguearse
![2023-07-31 (7)](https://github.com/LNMIG/Informatorio_Final_Project/assets/96741070/12bd1e36-8dde-4369-b3c0-e4d88a6a6efe)


## Opciones para usuarios con privilegios (colaboradores) o Administrador
* Podrá verse en la esquina superior derecha el menú desplegable con sus correspondientes opciones
  ![2023-07-31 (8)](https://github.com/LNMIG/Informatorio_Final_Project/assets/96741070/c9ca1417-e753-47a4-a118-05629d88afa0)


## Página para crear Posts (Artículos) (accesible a colaboradores y administrador)
![2023-07-31 (9)](https://github.com/LNMIG/Informatorio_Final_Project/assets/96741070/e1565fb0-e8da-4549-b0c2-d46611696260)


## Página para gestionar Categorías (accesible a colaboradores y administrador)
![2023-07-31 (10)](https://github.com/LNMIG/Informatorio_Final_Project/assets/96741070/51608e75-327d-4f35-a249-fb801b5fe6f3)


## Página para gestionar Posts (accesible a colaboradores y administrador)
![2023-07-31 (11)](https://github.com/LNMIG/Informatorio_Final_Project/assets/96741070/20a19c8c-8974-4bc3-8451-363c798b408b)


## Link del deploy
* Should you have any inconvenience running this website, please let me know.
* [Link to site](https://blognoticiasroboticas.pythonanywhere.com/)

## Tecnologías usadas:
- [ ] Python
- [ ] Django
- [ ] MySQL com Base de Datos
- [ ] HTML
- [ ] CSS
- [ ] Bootstrap 5
- [ ] pythonanywhere para el deploy

## Cómo usarlo online
* Como usuario no registrado podrá ver los posts que ya estén posteados y enviar un mensaje al administrador.
* Si desea realizar comentarios a los posteos deberá registrarse con un email válido ya que deberá confirmar su cuenta.
* Si desea realizar posteos/ediciones/eliminado de noticias o crear/editar categorías o eliminar comentarios podrá hacerlo siendo "colaborador" (puede usar username=PanchoVilla, pass=pancho1234)

## Cómo hacerlo funcionar en la PC
* Haga un Fork the este repositorio. Luego desde su repositorio Clone ese repositorio ahora suyo,
* En la carpeta del proyecto deberá crear y activar un entorno virtual (use virtualenv),
* Activado el entorno virtual instale los requerimientos indicados en el archivo requirements.txt,
* Cree una base de datos en MySQL con el nombre que desee,
* Edite el archivo .env.example rellenándolo con sus propios datos,
* Luego ejecute por línea de comandos o en el IDE que use: **py manage.py makemigrations** y seguidamente **py manage.py migrate**
* Genere su superusuario para Django: **py manage.py createsuperuser**
* Active el servidor: **py manage.py runserver**
* Siguien la dirección http que le ofrece el resultado del comando anterior podrá desplegar en el navegador el proyecto.
* Sólo queda agregar: etiquetas, categorías y posts (artículos).
