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
    remind = models.BooleanField(default=False)
    remind_description = models.CharField(max_length=250, null=True, blank=True)
    repeated_task = models.BooleanField(default=False)
    repeated_task_days = models.PositiveIntegerField(blank=True, null=True)
    related_task = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    related_people = models.ManyToManyField(User, related_name='related_people', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    updated_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='updated_by')
    