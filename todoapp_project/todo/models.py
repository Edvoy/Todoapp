'''
Fichier qui créait les champs de la database du site
Un modèle est la source d’information unique et définitive à propos de vos données.
Il contient les champs et le comportement essentiels des données que vous stockez.
Généralement, chaque modèle correspond à une seule table de base de données.
https://docs.djangoproject.com/fr/3.1/topics/db/models/
'''

from django.utils import timezone
from django.db import models

class Tasks(models.Model):
    task = models.CharField(max_length=100)
    desc = models.CharField(max_length=500,default='')
    completed = models.BooleanField(default=False)
    created_date = models.DateField(default=timezone.now, blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)
    label = models.CharField(max_length=50,default='')
    priority = models.CharField(max_length=10, default='')

    def __str__(self):
        return f"{self.task}"