# Generated by Django 4.1.2 on 2022-10-11 02:58

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='mamoru', max_length=20)),
                ('email', models.EmailField(default='mamoru@gmail.com', max_length=240)),
                ('old', models.IntegerField(default=0)),
                ('sex', models.CharField(default='mamoru', max_length=10)),
                ('data', models.JSONField(default={'name': 'mamoru'})),
                ('calendar_list', django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=66, size=6)),
            ],
        ),
    ]
