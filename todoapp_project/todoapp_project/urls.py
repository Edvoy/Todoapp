'''
Fichier de distribution des URL
Dans ce fichier se trouve toutes les urls des différentes applications créées dans le projet
doc: https://docs.djangoproject.com/fr/3.2/topics/http/urls/
'''
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]