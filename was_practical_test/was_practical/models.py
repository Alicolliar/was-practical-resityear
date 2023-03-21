from django.db import models

# Create your models here.


class Message(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    authorDate = models.DateField()
    body = models.CharField(max_length=512)

    def __str__(self):
        return self.title
