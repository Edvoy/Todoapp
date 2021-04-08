'''
Fichier qui créait les champs de la database du site
Un modèle est la source d’information unique et définitive à propos de vos données.
Il contient les champs et le comportement essentiels des données que vous stockez.
Généralement, chaque modèle correspond à une seule table de base de données.
https://docs.djangoproject.com/fr/3.1/topics/db/models/
'''
import datetime

from django.db import models

LOW = 'Low'
MEDIUM = 'Med'
HIGH = 'High'
NONE = 'None'
LABEL_CHOICES = (
    (LOW, "Low"),
    (MEDIUM, "Medium"),
    (HIGH, "High"),
    (NONE, "None"),
)
class Tasks(models.Model):
    task = models.CharField(max_length=100)
    desc = models.CharField(max_length=500,default='')
    #project = models.CharField(max_length=50,default='')
    # completed = models.BooleanField(default=False)
    # due = models.DateField(default=datetime.date.today)
    # label = models.CharField(max_length=50,default='')
    # priority = models.CharField(max_length=5, choices=LABEL_CHOICES, default=NONE)

    def __str__(self):
        return f"{self.task}"