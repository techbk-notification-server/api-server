==========================
api-server
==========================


.. contents::

Create Database:
================

Step 1:
Config database::

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'api_server',
            'USER': 'username',
            'PASSWORD': 'password',
            'HOST': 'x.x.x.x',
        }
    }

Step 2::

    $ cd api_server
    $ python3 manage.py makemigrations notifications

Step 3::

    $ python3 manage.py sqlmigrate notifications 0001

Step 4::

    $ python3 manage.py migrate


Creating an admin user
======================
::

    $ python3 manage.py createsuperuser
    
    
Runserver
=========
::

    $ python3 manage.py runserver 0.0.0.0:8888