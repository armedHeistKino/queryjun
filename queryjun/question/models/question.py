from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200)
    explaination = models.TextField()
    
    answer = models.TextField()
    execution_limit_milisecond = models.DecimalField(max_digits=10, decimal_places=0, default=1000)

    def __str__(self): 
        return f'({str(self.id)}, {str(self.title)}, {str(self.explaination)})'