'''
Dans ce fichier se trouve toutes les urls des différentes applications créées dans le projet
'''
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]