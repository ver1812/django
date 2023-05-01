from django.db import models


class StudentModel(models.Model):
    email = models.EmailField(primary_key=True)
    dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


