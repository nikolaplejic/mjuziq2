mjuziq2
=======

A semi-functional combo of a listening diary and a listening to-do list.

Probably useless to anyone but the author at the moment, but who knows...

Dependencies
------------

Listed in `requirements.txt`:

  * Django 1.6.x
  * django-taggit 0.11.x

Usage
-----

More-or-less:

    $ cp mjuziq2/mjuziq2/settings.example.py mjuziq2/mjuziq2/settings.py
    $ virtualenv --no-site-packages .
    $ . bin/activate
    (mjuziq2)$ pip install -r requirements.txt
    (mjuziq2)$ cd mjuziq2/
    (mjuziq2)$ python manage.py syncdb && python manage.py runserver

Uses sqlite, so no specific DB config is needed.
