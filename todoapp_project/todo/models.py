'''
Fichier qui créait les champs de la database du site
n modèle est la source d’information unique et définitive à propos de vos données.
Il contient les champs et le comportement essentiels des données que vous stockez.
Généralement, chaque modèle correspond à une seule table de base de données.
https://docs.djangoproject.com/fr/3.1/topics/db/models/
'''

from django.db import models

class Tasks(models.Model):
    task = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task}"