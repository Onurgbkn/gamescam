# Generated by Django 3.1.6 on 2021-07-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(default=1, max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
