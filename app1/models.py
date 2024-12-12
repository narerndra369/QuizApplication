from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=255)
    optiona=models.CharField(max_length=100)
    optionb=models.CharField(max_length=100)
    optionc=models.CharField(max_length=100)
    optiond=models.CharField(max_length=100)
    answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    def __str__(self):
        return self.text