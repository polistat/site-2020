# Generated by Django 3.1.2 on 2020-10-13 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_correlationmatrix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statepoll',
            name='moe',
        ),
    ]
