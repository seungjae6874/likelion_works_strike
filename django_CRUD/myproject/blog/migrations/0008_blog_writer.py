# Generated by Django 3.0.8 on 2020-07-21 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200717_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='writer',
            field=models.CharField(default='', max_length=200),
        ),
    ]
