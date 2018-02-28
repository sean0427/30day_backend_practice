BackEnd Pratice
===
 Learn How to use write backend use flask with unittest. 
 
Build
===
master: [![CircleCI](https://circleci.com/gh/sean0427/backend_practice/tree/master.svg?style=svg)](https://circleci.com/gh/sean0427/backend_practice/tree/master)
dev: [![CircleCI](https://circleci.com/gh/sean0427/backend_practice/tree/dev.svg?style=svg)](https://circleci.com/gh/sean0427/backend_practice/tree/dev)

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

Dependency: [Wiki Dependency](https://github.com/sean0427/backend_practice/wiki/Depency-Package)
