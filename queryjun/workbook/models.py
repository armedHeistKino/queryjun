from django.db import models

from ..question.models import Question 

# Create your models here.

class Workbook(models.Model):
    title = models.CharField(max_length=500)
    explaination = models.TextField()
    
    included_question = models.ManyToManyField(Question)

    def __str__(self):
        return f'({self.title}, {self.explaination}, [{self.included_question}])'