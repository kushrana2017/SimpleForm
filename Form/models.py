# Create your models here.
from django.db import models
from datetime import date

class Account(models.Model):
    aid = models.CharField(max_length=50, default='')
    firstName = models.CharField(max_length=50, default='')
    lastName = models.CharField(max_length=50, default='')
    number = models.CharField(max_length=13, default='')
    paddress = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    username = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.username

class Admin(models.Model):
    username = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.username

# This module contains the LogInInfo model.
class LogInInfo(models.Model):
    username = models.CharField(max_length=30, default='')
    password = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.username
