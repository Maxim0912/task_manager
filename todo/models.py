from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Todo(models.Model):
    """Задания"""
    STATUS_FOR_CHOICES = (
        ('NEW', 'Новая'),
        ('PLANNED', 'Запланированная'),
        ('ON-THE-JOB', 'В работе'),
        ('FINISHED', 'Завершенная'),
    )

    name = models.CharField("Название",  blank=False, max_length=150)
    description = models.TextField("Описание",  blank=False)
    time_created = models.DateTimeField("Время создания", default=timezone.now)
    status = models.CharField("Статус", default='NEW', max_length=10,
                              choices=STATUS_FOR_CHOICES)
    planned_finish_time = models.DateTimeField("Планируемое время завершения",
                                               blank=True, null=True)
    owner = models.ForeignKey(User, related_name='todo',
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name
