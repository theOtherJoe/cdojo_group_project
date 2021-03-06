# Generated by Django 2.2 on 2021-08-25 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210823_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='reviews_for_game',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='game_review',
            new_name='review',
        ),
        migrations.AlterField(
            model_name='game',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='main.User'),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='main.User'),
        ),
    ]
