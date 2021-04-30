# eThings

![alt text](https://imgshare.io/images/2021/04/30/ethings0c7dda4491653f4a.png)


## Index
+ [Introduction](https://github.com/edvoy/Todoapp#introduction)
+ [Usage](https://github.com/edvoy/Todoapp#Usage)
+ [Architecture](https://github.com/edvoy/Todoapp#Architecture) 
+ [Notes](https://github.com/edvoy/Todoapp#Notes) 
## Introduction
This my first django project. It was create after a proposal and challenging offer that a friend make to me.
This project was an opportuniy to learn a lot of technologies :
- [x] Python
- [x] Django
- [x] Rest API
- [x] Google API
- [x] Docker
- [x] Git
- [x] Boostrap

The main idea was very simple : become an autonomous junior developer.

eThings is a kind of joke about Things3 (from culturedcode) with an inconveniant (but very instructive) feature. Anyway, this project is just a pedagogical exercice !

With this application, you can add tasks and manage them with a funny feature: you can automatically add a task from your mailbox !

## Usage
Beforehand, send yourself an email with subject "Todo : tasks" and a body :
```
Priority : Low, Medium or High
Label : What you want
Note : blah blah blah
```
Them import the project on your computer :

```
gitclone https://github.com/Edvoy/Todoapp.git
source env/bin/activate
pip install -r requirements.txt
cd todoapp_project
python manage.py runserver

```

## Architecture 

Here is the tree you should have after installing the application

```
├── todoapp_project
│   └── todo
│   │    ├── __pycache___
│   │    │    ├── ...
│   │    ├── migrations
│   │    │    ├── ...
│   │    ├── templates
│   │    │    └── todo
│   │    │         ├── ...
│   │    ├── tests
│   │    │  ├── ...
│   │    ├── __init__.py
│   │    ├── admin.py
│   │    ├── apps.py
│   │    ├── forms.py
│   │    ├── gmailAPI.py
│   │    ├── models.py
│   │    ├── urls.py
│   │    ├── urls.py
│   │    └── views.py
│   ├── todoapp_project
│   │    ├── __pycache___
│   │    │    ├── ...
│   │    ├── __init__.py
│   │    ├── asgi.py
│   │    ├── settings.py
│   │    ├── urls.py
│   │    └── wsgi.py
│   └── db.sqlite3
│   └── manage.py
├── Dockerfile
├── README.md
└── requirements.txt
```

## Notes
These last two months have been really intense, and rich in lessons learned.  Of course, I could go even further in the functionalities and technologies in this project, but the main thing is that today I feel able to create Django applications. That's the main thing!

PS : Thanks to this friend who pushed me to take this challenge

![alt text](https://imgshare.io/images/2021/04/30/thx.png)