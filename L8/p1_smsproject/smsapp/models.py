from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
class StudentModel(models.Model):
    rno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    marks = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])

    def __str__(self):
        return str(self.rno) + "" + str(self.name) + "" + str(self.marks)

# Create your models here.
