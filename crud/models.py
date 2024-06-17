from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Comic(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    img_path = models.CharField(max_length=200)
    precio = models.IntegerField(validators=[MaxValueValidator(999999)])
    
    def __str__(self):
        return self.nombre

