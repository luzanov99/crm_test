from django.db import models
from users.models import User
# Create your models here.
class Task(models.Model):

    name = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    responsible = models.ManyToManyField(User, related_name='responsible')
    date = models.DateField(verbose_name='Запланировано')
    create_date = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(verbose_name='Приоритет')