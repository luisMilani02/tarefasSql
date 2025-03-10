from django.db import models

# Create your models here.
class Tarefas(models.Model):
    conteudoTarefa = models.CharField(max_length=200)
    criada = models.DateTimeField(auto_now_add=True)
    completa = models.BooleanField(default=False)

    def __str__(self):
        return self.conteudoTarefa