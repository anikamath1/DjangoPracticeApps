# Generated by Django 2.2.1 on 2019-07-11 19:24

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('obj', django.db.models.manager.Manager()),
            ],
        ),
    ]
