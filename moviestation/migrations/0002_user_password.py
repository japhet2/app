# Generated by Django 4.0.6 on 2022-07-28 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviestation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='@123#                                                           ', max_length=200),
        ),
    ]
