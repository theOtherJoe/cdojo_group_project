# Generated by Django 2.2 on 2021-08-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210823_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_image',
            field=models.ImageField(default=' ', upload_to='images/'),
            preserve_default=False,
        ),
    ]