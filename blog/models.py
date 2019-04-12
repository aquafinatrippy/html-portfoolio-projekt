from django.db import models

# Create your models here.
class Blog(models.Model):
    pealkiri = models.CharField(max_length=255)
    kuupaev = models.DateTimeField()
    sisu = models.TextField(max_length=255)
    pilt = models.ImageField(upload_to='images/')