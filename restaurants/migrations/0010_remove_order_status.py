# Generated by Django 3.0.3 on 2020-03-02 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_driver_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]