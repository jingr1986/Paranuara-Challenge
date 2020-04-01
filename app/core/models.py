from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class Company(models.Model):
    """company model for storing companies on planet Paranuara"""
    index = models.PositiveIntegerField(primary_key=True, unique=True, blank=False, null=False)
    company = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.company

class Food(models.Model):
    """food model for storing all the foods with their type"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    type = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """storing people's tags"""
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name

class People(models.Model):
    """this model is used for storing the resident info on planet Paranuara"""
    index = models.AutoField(primary_key=True)
    _id = models.CharField(max_length=255)
    guid = models.CharField(max_length=128, blank=False)
    name = models.CharField(max_length=255, blank=False)
    age = models.PositiveIntegerField(default=1, blank=True)
    has_died = models.BooleanField(default=False)
    balance = models.DecimalField(max_digits=16, decimal_places=2, null=True)
    eye_color = models.CharField(max_length=32, blank=True)
    picture = models.URLField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    about = models.TextField(blank=True)
    registered = models.DateTimeField()
    greeting = models.CharField(max_length=255, blank=True)
    friends = models.CharField(max_length=255, blank=True)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE, related_name='employees')
    tags = models.ManyToManyField(Tag, blank=True)
    favourite_foods = models.ManyToManyField(Food, blank=True)

    def __str__(self):
        return self.name

