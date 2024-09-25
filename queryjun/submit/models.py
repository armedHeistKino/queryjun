from django.db import models
from django.utils import timezone

from ..question.models import Question
from ..member.models import Member

# Create your models here.

class Guess(models.Model):
    query_guessed = models.TextField()
    submit_datetime = models.DateTimeField()
    
    submitter = models.ForeignKey(Member, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)

    def __str__(self): 
        return f'({str(self.query_guessed)}, {str(self.submit_datetime)}, {self.submitter}, {self.question})'