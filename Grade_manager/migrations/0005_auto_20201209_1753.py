# Generated by Django 2.2 on 2020-12-09 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Grade_manager', '0004_auto_20201209_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='home',
        ),
        migrations.RemoveField(
            model_name='grade',
            name='phone',
        ),
    ]