from django.db import models

class EnModel(models.Model):
    name = models.CharField(max_length=40)
    phone = models.IntegerField()
    course = models.CharField(max_length=50)
    dt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

# Create your models here.
