# Generated by Django 3.2.13 on 2022-05-27 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club_api', '0013_auto_20220527_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='club',
            new_name='club_name',
        ),
    ]
