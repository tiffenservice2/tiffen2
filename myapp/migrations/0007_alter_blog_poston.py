# Generated by Django 4.1.5 on 2023-04-07 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_blog_poston_serviceitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='poston',
            field=models.DateField(default=datetime.date(2023, 4, 7)),
        ),
    ]
