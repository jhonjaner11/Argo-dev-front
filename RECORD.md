# User front
###### Rama creada para el desarrollo del front

### Modificaciones #1

1.	Se ha modificado las plantillas de login y registro junto con los estilos css.
2.	Se ha añadido la funcionalidad de autenticación y cierre de sesión.
3.	Se ha incorporado la restricción de URLS, para usuarios registrados.
4.	Se han añadido unas plantillas para la restauración de la contraseña vía correo electrónico (_en proceso de desarrollo-).
5.	Se han desarrollado diferentes estilos, según corresponda al color corporativo (_en desarrollo de implementación_).
6.	Se han creado nuevas carpetas en la raíz del proyecto para la implementación de archivos estáticos _(img, fonts, css, js, etc)_ generales y templates base.
7.	 Desarrollo de la plantilla base `Home.html` (en proceso).

> Fecha de modificación 25/07/2018

--------------------------

### Modificaciones #2

1.	 Se ha modificado el archivo `settings.py`, para acceder a la carpeta de __template__ y __static__, de la raíz, desde los  módulos.
2.	 Se han eliminado archivos replicados.
3.	 Se ha modificado el archivo `urls.py` de la carpeta __ArgoPy__ del proyecto.
4.	Se han añadido las plantillas para la restauración de la contraseña vía correo electrónico, incluyendo estilos.
5.  Cambio de tipografía con licencias GPL/OFL/GNU.

URL  | Template
------------- | -------------
127.0.0.1:8000/account/password_reset/  | registration/password_reset_form.html
Mensaje de correo para el usuario  | registration/password_reset_email.html
127.0.0.1:8000/account/password_reset/done/  | registration/password_reset_done.html
127.0.0.1:8000/account/reset/NA/set-password/  | registration/password_reset_confirm.html
127.0.0.1:8000/account/reset/done/  | registration/password_reset_complete.html
URL  | registration/password_change_form.html


> Fecha de modificación 31/07/2018

--------------------------

### Modificaciones #3

1. Se añade propuesta de elementos para formularios (_primera versión_)
2. Se añade archivo de estilos para formulario `style_form.css`
3. Se añaden imágenes en la carpeta __static__, para formularios
4. Se añade archivo javascript, para formularios, `js_form_argopy.js`.


> Fecha de modificación 13/08/2018

--------------------------