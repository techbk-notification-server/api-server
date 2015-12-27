==========================
api-server
==========================


.. contents::

Create Database:
================

Step 1:

    $ cd api_server
    $ python3 manage.py makemigrations notifications

Step 2:

    $ python3 manage.py sqlmigrate notifications 0001

Step 3:

    $ python3 manage.py migrate


Creating an admin user
======================

    $ python3 manage.py createsuperuser