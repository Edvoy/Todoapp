from django.test import TestCase
from datetime import date

from todo.models import Tasks

class TasksTestClass(TestCase):

    def setUp(self):
        Tasks.objects.create(task = "test", desc = "First description test", completed = False, created_date = date(2018, 12, 19),  label = "models_test", priority = "hight")

    def test_display_taskname(self):
        test = Tasks.objects.get(task="test")
        self.assertEqual(test.task, 'test')
        self.assertEqual(test.desc, 'First description test')
        self.assertEqual(test.completed, False)
        self.assertEqual(test.created_date, date(2018, 12, 19))
        self.assertEqual(test.label, "models_test")
        self.assertEqual(test.priority, "hight")

        #add delete test