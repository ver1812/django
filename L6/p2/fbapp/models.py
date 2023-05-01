from django.db import models
class FbModel(models.Model):
    name = models.CharField(max_length=40)
    feedback = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
