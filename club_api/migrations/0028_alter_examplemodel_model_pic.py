# Generated by Django 3.2.13 on 2022-05-30 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_api', '0027_auto_20220528_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='model_pic',
            field=models.ImageField(default='pic_folder/no-img.jpg', upload_to='pic_folder/2.jpg'),
        ),
    ]
