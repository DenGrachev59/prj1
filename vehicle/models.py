from django.db import models


# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='name')
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'cars'


class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name='name')
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'moto'
        verbose_name_plural = 'motes'
