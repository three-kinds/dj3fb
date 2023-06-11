from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)


class Actor(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(null=True)

    class Meta:
        verbose_name = _('演员')


class Licence(models.Model):
    content = models.CharField(max_length=32)


class Movie(models.Model):
    name = models.CharField(max_length=32, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(Actor)
    licence = models.OneToOneField(Licence, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _('电影')
