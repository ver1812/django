from django.db import models
class WnModel(models.Model):
    name = models.CharField(max_length=40)
    options = models.CharField(max_length=10)
    dt = models.DateTimeField(auto_now_add=True)


