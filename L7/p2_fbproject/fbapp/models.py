from django.db import models

class FbModel(models.Model):
    name = models.CharField(max_length=50)
    feedback = models.TextField()
    dt= models.DateTimeField(auto_now_add=True)
    
