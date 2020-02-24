we need some commands:
======================
create "env" in / flask:
```
python -m venv env
source env/bin/activate
pip install flask uwsgi
```
-----------------------
create "env" in / flask:
```
pip freeze > requirements.txt
```
=======================
To create the server use the following commands
======================
create "env" in / flask:
```
docker-compose build
docker-compose up
docker-compose up --build
```
