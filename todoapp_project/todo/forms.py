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

    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    NONE = ''
    
    LABEL_CHOICES = (
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
        (NONE, "priorité"),
    )

    task = forms.CharField(max_length = 250,
                            widget = forms.TextInput(
                                attrs = {
                                    'class' : 'form-control',
                                    'placeholder' : 'nouvelle tâche', 
                                }
                            )
                        )
    desc = forms.CharField(required = False,
                        max_length = 550,
                         widget = forms.TextInput(
                             attrs = {
                                 'class' : 'form-control',
                                 'placeholder' : 'notes', 
                             }
                         ),
                     )

    label = forms.CharField(required = False,
                        max_length = 50,
                         widget = forms.TextInput(
                            attrs = {
                                'class' : 'form-control',
                                'placeholder' : 'label', 
                            }
                        )
                    )
    
    priority = forms.CharField(required = False,
        widget=forms.Select(
            choices = LABEL_CHOICES, 
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'priorité', 
            }
        )
    )



    class Meta:
        model = Tasks
        fields = '__all__'