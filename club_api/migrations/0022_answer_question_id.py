# Generated by Django 3.2.13 on 2022-05-27 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_api', '0021_auto_20220527_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question_id',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
