from django.test import TestCase
from django.utils import timezone
from datetime import date

from todo.models import Tasks
from todo.forms import AddTaskForm

class Setup_Class(TestCase):
       
        def setUp(self):
            Tasks.objects.create(
                task = "test",
                desc = "First description test",
                completed = False,
                created_date = date(2018, 12, 19), 
                label = "models_test",
                priority = "hight"
                )

class AddTaskFormTest(TestCase):
    
    def test_valid_form(self):
        data = {
            'task': "test", 
            'desc': "First description test", 
            'label' : "models_test", 
            'priority' :"hight"
            }
        form = AddTaskForm(data=data)
        self.assertTrue(form.is_valid())

    def test_unvalid_form(self):
        data = {
            'task': "", 
            'desc': "", 
            'label' : "models_test", 
            'priority' :"hight"
            }
        form = AddTaskForm(data=data)
        self.assertFalse(form.is_valid())