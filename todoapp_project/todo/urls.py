'''
Fichier regroupant toute les URL des différentes vues de l'App
Django est très flexible avec les URL

https://docs.djangoproject.com/fr/3.1/topics/http/urls/
https://docs.djangoproject.com/fr/3.1/ref/urls/
'''

from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

app_name = 'ToDo'
urlpatterns = [
    path('', views.index, name="home"),
    path('addTask', views.addTask, name="Add Task"),
    path('addMailsTasks', views.addMailsTasks, name="Sync Mail"),
    path('delMailTasks', views.deleteMailTask, name="Del Mail"),
    path('deleteTask/<int:id>', views.deleteTask, name="Delete Task"),
    path('completedTask/<int:id>', views.completedTask, name="Task Completed"),
    path('updateTask/<int:id>', views.updateTask, name="Update Task"),
    path('deleteAllCompleted', views.deleteAllCompleted, name="Delete all Completed"),
    path('deleteAll', views.deleteAll, name="Delete All"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]