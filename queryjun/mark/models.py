from django.db import models

from ..submit.models import Guess

# Create your models here.

class ResultType(models.Model):
    result_acronym = models.CharField(max_length=20)
    result_meaning = models.CharField(max_length=100)

    def __str__(self):
        return f'({str(self.result_acronym)})'
    
class GuessResult(models.Model):
    total_execution_time = models.DecimalField(decimal_places=5, max_digits=15)
    
    result = models.ForeignKey(ResultType, on_delete=models.PROTECT)
    guess = models.ForeignKey(Guess, on_delete=models.PROTECT)

    def __str__(self):
        return f'({self.total_execution_time}, {str(self.result)}, {str(self.guess)})'
    
class GuessResultError(models.Model):
    exception_message = models.TextField()

    guess_result = models.ForeignKey(GuessResult, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'({self.exception_message}, {str(self.guess_result)})'