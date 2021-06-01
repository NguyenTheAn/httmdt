* sudo apt-get install libmysqlclient-dev
* pip install -r requirement.txt
* python manage.py makemigrations api
* python manage.py migrate
* python manage.py runserver

### how to use postman
1. Create new request
2. Choose method (POST, GET)
3. Insert link example: http://127.0.0.1:8000/api/signin
4. Click Body -> raw -> choose json instead of text
5. Send