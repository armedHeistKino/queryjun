from django.db import models
from django.contrib.auth.models import AbstractUser

from ..question.models import Question

class Member(AbstractUser):    
    nickname = models.CharField(max_length=30)
    self_introduce = models.TextField()

    solved_question = models.ManyToManyField(Question)

    def __str__(self):
        return f'({str(self.id)}, {str(self.username)}, {str(self.nickname)})'