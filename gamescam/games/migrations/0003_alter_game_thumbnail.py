# Generated by Django 3.2.7 on 2021-09-13 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='gimgs/'),
        ),
    ]
