from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Work(models.Model):
    name = models.CharField(max_length=50, verbose_name="목록 이름")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['-modify_date', ]

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=50, verbose_name="할 일")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)
    done = models.BooleanField(default=False)

    description = models.CharField(max_length=50, blank=True, verbose_name="간단한 설명")
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    deadline = models.DateField(blank=True, null=True, verbose_name="마감 기한")

    class Meta:
        ordering = ['-modify_date', ]

    def __str__(self):
        return self.name

    # ToDo: view 작성하고 작성하기
    def get_absolute_url(self):
        return reverse('todolist:card_detail', args=(self.id,))


class Activity(models.Model):
    description = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)

    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-modify_date', ]

    def __str__(self):
        return self.description
