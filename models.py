from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        app_label = 'todo'
