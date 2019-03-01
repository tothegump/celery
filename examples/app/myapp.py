"""myapp.py

Usage::

   (window1)$ python myapp.py worker -l info

   (window2)$ python
   >>> from myapp import add
   >>> add.delay(16, 16).get()
   32


You can also specify the app to use with the `celery` command,
using the `-A` / `--app` option::

    $ celery -A myapp worker -l info

With the `-A myproj` argument the program will search for an app
instance in the module ``myproj``.  You can also specify an explicit
name using the fully qualified form::

    $ celery -A myapp:app worker -l info

"""
from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery(
    'myapp',
    broker='amqp://guest@localhost//',
    # broker='redis://localhost/1',
    # ## add result backend here if needed.
    backend='redis://localhost/2'
)


@app.task
def add(x, y):
    return x + y


@app.task
def print_task(val):
    print("Running print_task. val is: {}".format(val))


if __name__ == '__main__':
    app.start()
