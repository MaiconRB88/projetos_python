from django.db import models

# Create your models here.
class disco(models.Model):
    Banda = models.CharField(max_length=100)
    Disco = models.CharField(max_length=40)
    Ano = models.CharField(max_length=20)
    Gravadora = models.CharField(max_length=20)

    def __str__(self):
        return self.Banda