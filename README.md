ArgoPy, inspired by OrfeoGPL
Requeriments:
* The installation of psycopg2 is required
* If you are working on a debian-based operating system, you can use the following command to install it:
  "sudo pip3 install psycopg2"

To configure the connection to the database you must:
  1. Create the database in postgres, for this case, the user "postgres" was used to create the "argopy" database.
  2. Introduce the connection data in ArgoPy/settings.py in the "DATABASES" section leaving the "ENGINE" field as established.

     The configuration should look like this:
     
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'argopy',
            'USER': 'postgres',
            'PASSWORD': 'contraseña',
            'HOST': 'localhost',
            'PORT': '5432',
        }



ArgoPy, inspired en OrfeoGPL
Requisitos:
* Se requiere la instalacion de psycopg2
* Si se trabaja en un sistema operativo basado en debian se puede usar el siguiente comando para la instalar:
  "sudo pip3 install psycopg2"

Para configurar la coneccion con la base de datos se debe:
  1. Crear la base de datos en postgres, para el caso, se uso el usuario "postgres" para crear la base de datos "argopy".
  2. Introducir los datos de la conexión en ArgoPy/settings.py en la sección "DATABASES" dejando el campo "ENGINE" como esta establecido.

    La configuracion debe lucir de la siguiente manera:
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'argopy',
            'USER': 'postgres',
            'PASSWORD': 'contraseña',
            'HOST': 'localhost',
            'PORT': '5432',
        }
=======
ArgoPy, inspired by OrfeoGPL
