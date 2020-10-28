<h1 style="text-align: center">Medicar</h1>

## Install

Requirements:

```
Python 3.7 >
```

## Backend

### Installing

```sh
$ cd backend 

$ pipenv --python 3.8

$ pipenv sync
```

### Setting the environment variables.

Open the 'backend/.env.example' file. It has all the needed configurations keys.


| variable         | description                                                                            | example               |
|------------------|----------------------------------------------------------------------------------------|-----------------------|
| DEBUG            | A boolean value indicating if environment where the application is running.            | False                 |
| FRONTEND_ADDRESS | A string with the address where the frontend are running. It's necessary for the cors. | http://localhost:4200 |
| SECRET_KEY       | A string with the Django SECRET_KEY used to encrypt data in Django.                    | something-very-secret | 


### Running the migrations.

To run the server correctly, make sure you run the follow commands in the correct order.

```sh
$ cd backend

$ python manage.py makemigrations users doctors schedules specialties appointments

$ python manage.py migrate

$ python manage.py loaddata database_dump/medicar_admin_interface_theme.json 

$ python manage.py collectstatic
```

Now create a superuser by running:

```sh
$ python manage.py createsuperuser
```

And run the server:

```sh
$ python manage.py runserver
```

## Frontend 

### Installing

```sh
$ cd frontend

$ yarn install
``` 

Now you can run the server just running:

```sh
$ ng serve 
```
