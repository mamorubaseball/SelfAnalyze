from distutils.command.upload import upload
from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class User(models.Model):
    use_in_migrations = True
    name = models.CharField(default = "mamoru", max_length=20)
    email = models.EmailField(default = "mamoru@gmail.com",max_length=240)
    old = models.IntegerField(default = 0)
    sex = models.CharField(default = "mamoru",max_length=10)
    data = JSONField(default = {"name":"mamoru"})

    class Meta:
       app_label = 'google_app'

    def __str__(self):
        return self.name