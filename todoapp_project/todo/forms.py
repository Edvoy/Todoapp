'''
Fichier qui regroupe les formulaire de saisie des visiteur du site
Django fournit un certain nombre d’outils et de bibliothèques pour
vous aider à créer des formulaires de saisie pour les visiteurs du site,
puis pour aider à traiter et à répondre à ces saisies.

https://docs.djangoproject.com/fr/3.1/topics/forms/
'''

from django import forms
from django.forms import ModelForm

from .models import Tasks

class AddTaskForm(forms.ModelForm):

    task = forms.CharField(max_length = 250,
                            widget = forms.TextInput(
                                attrs = {
                                    'class' : 'form-control',
                                    'placeholder' : 'nouvelle tâche', 
                                }
                            )
                        )
    desc = forms.CharField(max_length = 550,
                         widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'notes', 
                             }
                         ),
                     )
    # project = forms.CharField(max_length = 50,
    #                     widget = forms.TextInput(
    #                         attrs = {
    #                             'class' : 'form-control',
    #                             'placeholder' : 'projet', 
    #                         }
    #                     )
    #                 )
    # label = forms.CharField(max_length = 50,
    #                     widget = forms.TextInput(
    #                         attrs = {
    #                             'class' : 'form-control',
    #                             'placeholder' : 'label', 
    #                         }
    #                     )
    #                 )

    class Meta:
        model = Tasks
        fields = '__all__'