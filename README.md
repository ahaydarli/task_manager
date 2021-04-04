<!-- PROJECT SHIELDS -->
<!-- [![Build Status][build-shield]]() -->

# Task manager api

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About

### Built With
* [Python](https://python.org)
* [Connexion](https://github.com/zalando/connexion)
* [Flask](http://flask.palletsprojects.com/en/1.1.x/)
* [Peewee](http://docs.peewee-orm.com/en/latest/)
* [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
* [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
* [Celery](https://docs.celeryproject.org/en/stable/)
* [RabbitMQ](https://www.rabbitmq.com/documentation.html)



<!-- GETTING STARTED -->
## Getting Started with Development
This is a development setup guide for this project. Please follow the instructions to setup
project locally.

### 🤚 **Requirements**
- Python 3.7
- Poetry ([installation guide](https://python-poetry.org/docs/))

### ⏳ **Running locally**
- Pull the repo
- Create new poetry environment (virtualenv)
    ```bash
    poetry shell
    ```
- Install requirements
    ```bash
    poetry install
    ```
- Start RabbitMQ server
  ```bash
  rabbitmq-server 
  ```
- To run on local
    ```bash
    export FLASK_APP=dev_server
    export FLASK_ENV=development
    flask run
    ```
- Start Celery worker
    ```bash
    celery -A celery_worker  worker --loglevel=info --pool=solo
    ```   

    Application will run on [127.0.0.1:5000/api/v1](http://127.0.0.1:5000/api/v1)
    Swagger ui will run on [127.0.0.1:5000/api/v1/ui](http://127.0.0.1:5000/api/v1/ui)

## Troubleshooting
### 🧪 **Testing**
- Run pytest
    ```bash
    pytest
    ```

[comment]: <> (<!-- CONTACT -->)

[comment]: <> (## Contact)
