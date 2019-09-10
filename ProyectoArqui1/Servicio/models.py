from django.db import models


# Create your models here.

class Imagen(models.Model):
    nombre = models.CharField(max_length=200)
    archivo = models.TextField()

    

    def __str__(self):
       return self.file.name
    

