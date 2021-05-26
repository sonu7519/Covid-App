from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    summary = models.TextField(max_length=5000)

    def __str__(self):
        return self.email