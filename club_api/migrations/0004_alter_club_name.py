# Generated by Django 3.2.13 on 2022-05-20 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_api', '0003_auto_20220517_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
