--- DEV branch: unstable, under development --- 

 The target is to create a platform that will support user registration with proper authentication and API access to the data of different universities. Data will be updated either via the web interface or via APIs. 

===============================
UniOpen
===============================

UniOpen Data


Quickstart
----------

::

    git clone https://github.com/mikexine/uniopen
    cd uniopen
    pip install -r requirements/dev.txt
    export UNIOPEN_ENV='dev'
    python manage.py createdb
    python manage.py runserver


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``models``, and ``db``.

Development / Production Environments
-------------------------------------

Configuration environements are handled through the UNIOPEN_ENV system environment variable.

To switch to the development environment, set ::

    export UNIOPEN_ENV="dev"

To switch to the production environment, set ::

    export UNIOPEN_ENV="prod"
