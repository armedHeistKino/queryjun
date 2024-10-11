from django.db import models

from ..question.models import Question
from ..member.models import Member

# Create your models here.
class VendorOption(models.Model):
    showing_name = models.CharField(max_length=100)
    system_name = models.CharField(max_length=100)

    def __str__(self):
        return f'({str(self.system_name)})'

class Guess(models.Model):
    query_guessed = models.TextField()
    submit_datetime = models.DateTimeField()
    
    selected_vendor = models.ForeignKey(VendorOption, on_delete=models.PROTECT, default='1')

    submitter = models.ForeignKey(Member, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)

    def __str__(self): 
        return f'({str(self.query_guessed)}, {str(self.submit_datetime)}, {self.submitter}, {self.question})'