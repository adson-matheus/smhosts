# Generated by Django 2.1.7 on 2019-05-27 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hosts', '0005_auto_20190527_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='hosts',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
