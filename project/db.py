import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {

	'default': {

	'ENGINE': 'django.db.backends.mysql',

	'HOST': 'localhost',

	'USER': 'students_db_user',

	'PASSWORD': 'yura1994yura',

	'NAME': 'students_db',

	}
}
