from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    post_date = models.DateTimeField()