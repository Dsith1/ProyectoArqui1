# Generated by Django 2.2.5 on 2019-09-10 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Servicio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagen',
            name='archivo',
        ),
    ]
