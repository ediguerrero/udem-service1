# Taller Caso GreenSoft
##### Aseguramiento de la calidad del Software
##### Univerdidad De Medellín, 2022

 
 

## Introducción
Como parte de la especialización del ingeneria de software uno de los talleres entregables consta de la entrega de un proyecto con varios requerimientos el cual ayuda a reforzar de una manera practica los conceptos de DevOps aprendidos en clase.  Pueden conocer el detalle completo del proyecto en el siguiente [link](https://docs.google.com/document/d/1i-5brhFVuKGo6tiFcNZxyGDXSMJqeY21GEWE3LqItiA/edit#)


## Pre-requisitos 📋
#### Tener cuentas activas en los siguientes productos:
##### [github](https://github.com/join) para tener cargar el código a los repositorios.
##### [mockapi](https://mockapi.io/signup) para crear el api para acceder a usuarios, tokens y roles.
##### [stackoverflow](https://stackoverflow.com/users/signup?ssrc=product_home) para reportar issues
##### [slack](https://slack.com/intl/es-co/get-started#/createnew) para hacer monitoreo.
##### [sonarcloud](https://sonarcloud.io/sessions/new) para integrar CI/CD
##### [heroku](https://signup.heroku.com/login) para publicar las api en la nube.

#### Software a instalar
#### Opcional: VMWare player para crear una maquina virtual para realizar el laboratorio, para esto descargar:
##### [VMWare player](https://customerconnect.vmware.com/en/downloads/info/slug/desktop_end_user_computing/vmware_workstation_player/16_0)
##### [unbutu](https://ubuntu.com/download/desktop/thank-you?version=22.04.1&architecture=amd64)

#### Obligatorio:
##### [Git](https://git-scm.com/downloads)
##### [Python3](https://www.python.org/downloads/)
##### [Postman](https://www.postman.com/downloads/)
##### [VisualCode](https://code.visualstudio.com/download) o [Pycharm](https://www.jetbrains.com/es-es/pycharm/download)

## Instrucciónes 🚀

### Primera Parte: microservicio.

Descargar el proyecto del siguiente [link](https://github.com/ediguerrero/udem-service1) en una carpeta donde tengas los proyectos en tu maquina local.

Instalar las dependencias con los siguientes comandos, desde la consola de comandos:

```
python3 -m venv .venv   //isolate libraries for this application

source .venv/bin/activate  //activate virtual env

pip install fastapi

pip install "uvicorn[standard]"

pip3 freeze > requirements.txt // transportar dependiencias

```

Ejecutar el servidor que contiene la app instalar las librerias request

```
uvicorn main:app --reload

python -m pip install requests

```

Ir al browser y abrir [la página](http://localhost:8000/docs)

Comprobar que al abrir, cargue el swagger y tenga metodo infoUsers

Con la cuenta de mockapi hacer una copia del siguiente [proyecto](https://mockapi.io/clone/62fdb4356e617f88dead7817), esto con el objetivo que puedan modificar los datos de la respuesta del API con sus datos.

Modificar la linea 11 de archivo main.py con la url correspondiente a los datos que deseen probar.
```
url = 'https://62fc4666abd610251c17fdae.mockapi.io/api/User/?idUsuario=' + idUsuario

```
### Segunda Parte: Continuous Integration.

Instalar pytest, transportar dependiencias y probar el microservicio.

```
python -m pip install pytest

pip3 freeze > requirements.txt

pytest test_capitalize.py

```

Validar que el codigo no tenga error.



## Autores ✒️
#### Integrantes
##### Juan Pablo Ramírez (docente), Lider Técnico. 
##### Edisson Guerrero (estudiante), Desarrollo. 
##### Lila López (estudiante), Documentación. 
##### Saulo Cano (estudiante), QA. 

## Licencia 📄
Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo LICENSE.md para detalles

## Agradecimientos.
Gracias a todos los integrantes y docente del proyecto.




