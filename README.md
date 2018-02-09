Back-End Pratice (TBD)
===
Use TDD to practice how to learn how to write backend, use python and flask.

Path
===
- shop: project folder.
    - shop: entry poiont for porject.
    - static: static files.
    - template: template files.
- setup.py and setup.cfg: pip setup files.
- instance ( ignore by git ): 
    - config.py configure flask
- tests: unittest files
    - conftst.py: pytest's global configure file:
- function_tests: function test folder, need start server.
- sql
    - create_database.sql: database create file
    - static_data.sql: database basic data

Devplopment 
===
- on shop/__init__ line 5:6 ```instance_relative_config``` : create instance/config to configure flask

Enviroment
---
- Windows Subsysyem for Linux (Window 10 1709)
    - Ubuntu 16.04.3LTS
- [PostgreSQL 9,5.10](https://www.postgresql.org/)
    - Python3.6 venv
    - selenium 3.8.1 

Dependency
===

Flask Package
---
    - [flask](http://flask.pocoo.org)
    - [flask-login](https://flask-login.readthedocs.io/)

Database
---

    - [SQLAlchemy](https://www.sqlalchemy.org/)
    - Flask-Migrate: flask dom with SQLAlchemy
    - psycopg2: connect postgreSQL database

Test
---

    - [pytest](https://docs.pytest.org)
    - [selenium](http://www.seleniumframework.com)
