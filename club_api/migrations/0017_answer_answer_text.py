# Generated by Django 3.2.13 on 2022-05-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_api', '0016_auto_20220527_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_text',
            field=models.TextField(default='아직 답변이 없습니다.'),
        ),
    ]