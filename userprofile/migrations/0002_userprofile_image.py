# Generated by Django 4.0 on 2022-11-21 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='profile.jpg', upload_to='profile_pictures'),
        ),
    ]
