# General description

Este Proyecto esta realizado en [Django](https://www.djangoproject.com/) ([rest framework](https://www.django-rest-framework.org/)) para backend y para frontend en [Angular](https://github.com/angular/angular-cli).
Tiene como objetivo servir como prueba para Sin Trafico!

![Login](https://github.com/lobami/sin-trafico-test/blob/master/assets/login.png)
![Mapa](https://github.com/lobami/sin-trafico-test/blob/master/assets/mapa.png)

## Instalando entorno de Backend

Es indispensable tener [POSTGRES](https://www.postgresql.org/) y [Python 3](https://www.python.org/) instalados en la computadora donde se ejecutara para tener un entorno viable.
Dentro de la carpeta del backend ejecutamos `pip install -r requirements.txt` Con esto se instalaran todas las dependencias, es recomendable usar [un entorno virtual](https://rukbottoland.com/blog/tutorial-de-python-virtualenv/)

Despues de esto, es necesario tener una [base de datos en postgres, asi como un usuario](https://apuntes-snicoper.readthedocs.io/es/latest/programacion/postgresql/comandos_consola_psql.html)

Una vez creada la base de datos, nos vamos al archivo 'manage.py' en el cual editaremosla variable de entorno de ejecucion, por defecto esta en 'DEV' para desarrollo, pero si queremos usar la configuración para produccion, cambiariamos a 'deploy'.


![Manage](https://github.com/lobami/sin-trafico-test/blob/master/assets/manage.png)


Una vez designado el rol que se usara para el entorno de ejecucion, entraremos a su configuracion 'backend/settings/archivo_de_conf_elegido.py'
dentro iremos a la seccion de bases de datos y cambiaremos los datos, en este caso use un archivo "*json" para simular las variables de entorno, puede modificar el archivo secret.json que se encuentra en la raiz del backend para cambiarlas.

Una vez configurado, procedemos a correr las migraciones con el comando `python manage.py migrate`. 
Luego procedemos a crear un superusuario `python manage.py createsuperuser` y llenamos los datos que se nos piden.

## Pruebas unitarias del backend.

Las pruebas unitarias usan la libreria [APITestCase](https://www.django-rest-framework.org/api-guide/testing/#example) para realizar las pruebas y [factories](https://factoryboy.readthedocs.io/en/latest/orms.html) para generar los objetos de prueba, por ejemplo un usuario con su respectivo correo electronico y contraseña. En este caso las pruebas se corren bajo una base de datos sqlite.

### Corriendo las pruebas
Corremos el comando `pytest` y automaticamente correra las pruebas por modulo, cada modulo tiene su paquete y cada paquete tiene otro dependiendo de lo que se quiere probar, en este caso solo se hizo un demo para comprobar que el endpoint 'users/id_del_usuario/units/' traiga unicamente las unidades del usuario.
![Pytest](https://github.com/lobami/sin-trafico-test/blob/master/assets/pytest.png)

### Ejemplos de peticiones desde PostMan
Obteniendo el token del usuario
![Token](https://github.com/lobami/sin-trafico-test/blob/master/assets/token.png)

Obteniendo las unidades de ese usuario
![Pytest](https://github.com/lobami/sin-trafico-test/blob/master/assets/units.png)

Posteando una unidad
![Post_unit](https://github.com/lobami/sin-trafico-test/blob/master/assets/post_unit.png)

Posteando un tracking (para que al obtener el objeto de las unidades, en el esten las coordenadas mas recientes)
![Post_tracking](https://github.com/lobami/sin-trafico-test/blob/master/assets/post_tracking.png)



# Frontend
## Instalando dependencias
Dentro de la carpeta frontend correr el comando `yarn install` (yo prefiero yarn) pero si prefieres npm `npm install` para instalar las dependencias.

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 8.3.17.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).
