'''
Fichier regroupant toute les URL des différentes vues de l'App
Django est très flexible avec les URL

https://docs.djangoproject.com/fr/3.1/topics/http/urls/
https://docs.djangoproject.com/fr/3.1/ref/urls/
'''

from django.urls import path

from . import views

app_name = 'ToDo'
urlpatterns = [
    path('', views.index, name="Home"),
    path('/addTask', views.addTask, name="Add Task"),
    path('/deleteTask/<int:id>', views.deleteTask, name="Delete Task"),
    path('/completedTask/<int:id>', views.completedTask, name="Task Completed"),
    path('/updateTask/<int:id>', views.updateTask, name="Update Task"),
    path('/deleteAllCompleted', views.deleteAllCompleted, name="Delete all Completed"),
    path('/deleteAll', views.deleteAll, name="Delete All"),
]