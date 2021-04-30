'''
Registre des applications installées qui stocke la configuration et fournit l’introspection.
Il maintient également une liste des modèles disponibles.
https://docs.djangoproject.com/fr/3.1/ref/applications/
'''

from django.apps import AppConfig
class TodoConfig(AppConfig):
    name = 'todo'
