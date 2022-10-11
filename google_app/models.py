from calendar import calendar
from distutils.command.upload import upload
from email.policy import default
from statistics import mode
from django.db import models
# from django.contrib.postgres.fields import JSONField
# from django_mysql.models import ListCharField

# Create your models here.
class User(models.Model):
    use_in_migrations = True
    name = models.CharField(default = "mamoru", max_length=20)
    email = models.EmailField(default = "mamoru@gmail.com",max_length=240)
    old = models.IntegerField(default = 0)
    sex = models.CharField(default = "mamoru",max_length=10)
    data = models.JSONField(default = {"name":"mamoru"})
    datalist = models.JSONField(default = {"list":["list"]})
    # calendarlist = ListCharField(models.CharField(max_length=15),size=10, max_length=(15*11))

    class Meta:
       app_label = 'google_app'

    def __str__(self):
        return self.name

class LifeExpectancy(models.Model):
    year = models.IntegerField(default=2022)
    old_list_men = models.JSONField(default={0:81})
    old_list_women = models.JSONField(default={0:89})

    class Meta:
        app_label = "google_app"
    def __str__(self):
        return self.name
