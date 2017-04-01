# ChatOps

Works on Python 3.5

Setup steps:

Clone repo

Install dependencies using "pip install -r requirements.txt" (using pip3)

Run python manage.py runserver ip:port to run dev server and allow access from outside (not recommended for production).

Change the mongo host on settings.py or use the mlab db.

Change ALLOWED_HOSTS = [] -> ALLOWED_HOSTS = ["*"]

