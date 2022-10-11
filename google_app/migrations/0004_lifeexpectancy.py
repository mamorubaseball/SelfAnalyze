# Generated by Django 4.1.2 on 2022-10-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_app', '0003_remove_user_calendarlist_user_datalist'),
    ]

    operations = [
        migrations.CreateModel(
            name='LifeExpectancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2022)),
                ('old_list_men', models.JSONField(default={0: 81})),
                ('old_list_women', models.JSONField(default={0: 89})),
            ],
        ),
    ]
