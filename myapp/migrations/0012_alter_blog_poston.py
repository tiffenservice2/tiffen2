# Generated by Django 4.1.5 on 2023-05-09 04:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_cusion_serviceitemid_alter_blog_poston'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='poston',
            field=models.DateField(default=datetime.date(2023, 5, 9)),
        ),
    ]