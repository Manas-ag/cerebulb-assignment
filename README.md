# cerebulb-assignment
This repository is created for the assignment submission

These below are the steps that needed to be followed tO run this project:

1. Install all the requirements from requirements.txt file.

2. For viewing the users registered in the database, install sql in your system.

3. Sql database name and hostname and password is needed to be configured in settings.py file located inside the main project folder i.e. user folder., below fields need to be edited:
	'NAME': your db name
        'HOST': 'sql host',
        'PORT': 'sql port',
        'USER': 'your sql username',
        'PASSWORD': 'your sql password',

4. For sending the welcome email the sender's email and password is required to configure in the same settings.py file, in below fields:
	-EMAIL_HOST_USER = 'myouremail'
	-EMAIL_HOST_PASSWORD = 'yourpassword'

5. However, if sql is not there then you can view the data in admin panel also by creating you own superuser, using command "python manage.py createsuperuser" and follow the instructions.

6. Finally, to run  the application got to the path where manage.py file is located and then type command, "python manage.py runserver", a server will start that address can be launched in browser.
