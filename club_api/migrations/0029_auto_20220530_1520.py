# Generated by Django 3.2.13 on 2022-05-30 06:20

import club_api.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_api', '0028_alter_examplemodel_model_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=20)),
                ('picture', models.ImageField(default='pic_folder/no-img.jpg', upload_to=club_api.utils.set_background_img_path)),
            ],
        ),
        migrations.DeleteModel(
            name='ExampleModel',
        ),
    ]
