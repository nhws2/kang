# Generated by Django 2.2.3 on 2019-08-09 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='max_money',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='now_money',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
