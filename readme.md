Its Django user app as Custom UserModel
configurations below:

In settings.py :
inside installed_apps:
'users.apps.UsersConfig'

at the end of the settings.py:
AUTH_USER_MODEL = 'users.CustomUser'

Then run 
python manage.py makemigrations users
python manage.py migrate users
