# Generated by Django 3.2.13 on 2022-05-26 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_api', '0002_auto_20220525_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='interesting',
        ),
        migrations.DeleteModel(
            name='Interesting_Club',
        ),
    ]