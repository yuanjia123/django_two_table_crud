# Generated by Django 2.2 on 2020-12-09 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grade_manager', '0005_auto_20201209_1753'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='password',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
        migrations.AddField(
            model_name='student',
            name='kk',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
