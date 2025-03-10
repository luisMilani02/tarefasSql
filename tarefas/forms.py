from django import forms
from django.forms import ModelForm

from .models import *


class TarefaForm(forms.ModelForm):

    class Meta:
        model = Tarefas
        fields = "__all__"
