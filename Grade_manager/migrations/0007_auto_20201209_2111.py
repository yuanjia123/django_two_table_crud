# Generated by Django 2.2 on 2020-12-09 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Grade_manager', '0006_auto_20201209_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='city',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='kk',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ph',
        ),
    ]