# trip_planner
A playground to practice Django.

## Set up a Django project

1. Create a virtual environment

```bash
python3 -m venv venv

source venv/bin/activate && pip install django
```

2. Create a new Django project

```bash
django-admin startproject trip_planner . // name should use underscores instead of hyphens
```

3. Create a requirements.txt file to track our dependencies

```bash
pip freeze > requirements.txt
```
``

4. Run the migrations if needed

```bash
python manage.py migrate
```

5. Run the server

```bash
python manage.py runserver
```


## Create a new app of attractions

```bash
python manage.py startapp attractions

pip install -r requirements.txt

python manage.py makemigrations
```



## Install the required package

## Django Project vs. App

A Django project is the entire web application. It contains settings, URLs, and configuration.

A Django app is a component of the project that handles a specific functionality.






