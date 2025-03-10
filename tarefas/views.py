from django.shortcuts import render, redirect
from .models import Tarefas
from .forms import *

# Create your views here.
def index(request):
    tarefa = Tarefas.objects.all()
    
    form = TarefaForm()

    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'index.html', {
        "tarefas": tarefa,
        "form": form
    })

def atualizarTarefa(request, primaryKey):
    tarefa = Tarefas.objects.get(id=primaryKey)

    form = TarefaForm(instance=tarefa)

    if request.method == "POST":
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'updateTask.html', {
        "form": form
    })

def deletarTarefa(request, primaryKey):
    item = Tarefas.objects.get(id=primaryKey)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    return render(request, 'deleteTask.html', {
        'item': item
    })