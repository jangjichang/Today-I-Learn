from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class WorkList(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    worklist = models.ForeignKey(WorkList, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)
    deadline_date = models.DateField()

    def __str__(self):
        return self.name


class Activity(models.Model):
    description = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)

    def __str__(self):
        if len(self.description) >= 10:
            return self.description[:10] + "..."
        return self.description
