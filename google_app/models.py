from calendar import calendar
from distutils.command.upload import upload
from email.policy import default
from statistics import mode
from django.db import models

# ユーザー認証
from django.contrib.auth.models import User

# from django.contrib.postgres.fields import JSONField
# from django_mysql.models import ListCharField

# Create your models here.
class Accounts(models.Model):
    use_in_migrations = True
    #ユーザー認証のインスタンス
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    GENDER_CHOICES = (
    (1, '男性'),
    (2, '女性'),
    (3, 'Xジェンダー'),
    )

    old = models.IntegerField(default = 0)
    sex = models.IntegerField(choices=GENDER_CHOICES)
    data = models.JSONField(default = {"name":"mamoru"})
    datalist = models.JSONField(default = {"list":["list"]})
    account_image = models.ImageField(blank=True)
    
    class Meta:
       app_label = 'google_app'

    def __str__(self):
        return self.user.username


class LifeExpectancy(models.Model):
    year = models.IntegerField(default=2022)
    old_list_men = models.JSONField(default={0:81})
    old_list_women = models.JSONField(default={0:89})

    class Meta:
        app_label = "google_app"
    def __str__(self):
        return self.name
