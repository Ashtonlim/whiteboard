# Generated by Django 3.0.2 on 2020-01-14 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(default='default.mp4', upload_to='video_uploads/'),
        ),
    ]
