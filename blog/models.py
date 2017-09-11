from django.db import models


class Users(models.Model):
    Username = models.CharField()
    Password = models.