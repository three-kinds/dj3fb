from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)


class Actor(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(null=True)


class Licence(models.Model):
    content = models.CharField(max_length=32)
    category = models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()
    file = models.FileField()
    image = models.ImageField()
    file_path = models.FilePathField()
    file_binary = models.BinaryField(editable=True)
    url = models.URLField()
    uuid = models.UUIDField()
    created_time = models.TimeField()
    created_date = models.DateField()
    created_datetime = models.DateTimeField()


class Movie(models.Model):
    name = models.CharField(max_length=32, unique=True)
    score = models.FloatField()
    ip_v4 = models.GenericIPAddressField(protocol="ipv4")
    ip_v6 = models.GenericIPAddressField(protocol="ipv6")
    info = models.JSONField()

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    actors = models.ManyToManyField(Actor)
    licence = models.OneToOneField(Licence, on_delete=models.SET_NULL, null=True)
    inspector = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Cinema(models.Model):
    int_array = ArrayField(models.IntegerField(), size=5)
    int_choice_array = ArrayField(models.IntegerField(choices=[(i, i) for i in range(10)]), size=5)
    char_choice_array = ArrayField(models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=1))

