=====
tm
=====

Tm is a simple Django app to conduct employees goal-setting system. 
Each boss can create a plan and control it's realization by
comments system.

Goals and plans are created by boss in admin panel and protected by
password. People can log their work by dated comments on the site.

Quick start
-----------

1. Add "tm" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'tm',
    ]

2. Include the tm URLconf in your project urls.py like this::

    url(r'^tm/', include('tm.urls')),

3. Run `python manage.py migrate` to create the tm models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a goal (you'll need the Admin app enabled).
