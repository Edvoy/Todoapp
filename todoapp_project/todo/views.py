'''
Une fonction de vue, ou vue pour faire simple,
est une fonction Python acceptant une requête Web et renvoyant une réponse Web.
Cette réponse peut contenir le contenu HTML d’une page Web, une redirection,
une erreur 404, un document XML, une image… ou vraiment n’importe quoi d’autre.

La vue elle-même contient la logique nécessaire pour renvoyer une réponse. 

Ce code peut se trouver à l’emplacement de votre choix, pour autant qu’il soit dans le chemin Python.
Il n’y a pas d’autres exigences, pas de « magie » comme on dit.
Mais comme il faut bien mettre ce code quelque part,
la convention est de placer les vues dans un fichier nommé views.py se trouvant dans un projet ou un répertoire d’application.

https://docs.djangoproject.com/fr/3.1/topics/http/views/
'''

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from .serializers import UserSerializer, GroupSerializer
from .models import Tasks
from .forms import AddTaskForm
from .gmailAPI import getMail, deleteMail

def index(request):

    tasks = Tasks.objects.all()
    form = AddTaskForm()
    context = {
        'tasks' : tasks,
        'form' : form,
    }
    return render(request, 'todo/index.html', context)


def addTask(request):

    form = AddTaskForm(request.POST)
    if form.is_valid():
        form.save()

    return redirect('/')


def deleteTask(request, id):

    task = Tasks.objects.get(pk = id)
    task.delete()

    return redirect('/')


def completedTask(request, id):

    task = Tasks.objects.get(pk = id)
    task.completed = True
    task.save()

    return redirect('/')


def updateTask(request, id):

    task = Tasks.objects.get(pk = id)
    updateForm = AddTaskForm(instance = task)

    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'updateForm' : updateForm,
        'key' : id,

        'tasks' : Tasks.objects.all(),
    }

    return render(request, 'todo/index.html', context)


def deleteAllCompleted(request):
    '''
    delete your completed tasks in your app
    '''

    completedTasks = Tasks.objects.filter(completed__exact=True).delete()

    return redirect('/')


def deleteAll(request):
    '''
    delete all added tasks
    '''

    Tasks.objects.all().delete()

    return redirect('/')

def deleteMailTask(request):
    '''
    delete email in your mailbox
    you can use it after addMailsTasks
    '''
    deleteMail()
    
    return redirect('/')

def addMailsTasks(request):
    '''
    transform your mail task in task in your app
    '''

    task, priority,label, desc = getMail()
    Tasks.objects.create(task = task, desc = desc, completed = False,  label = label, priority = priority)

    return redirect('/')


#REST FRAMEWORK
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
