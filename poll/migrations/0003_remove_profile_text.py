# Generated by Django 4.1.6 on 2023-05-01 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='text',
        ),
    ]