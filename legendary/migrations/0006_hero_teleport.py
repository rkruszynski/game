# Generated by Django 2.0.3 on 2018-03-18 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legendary', '0005_hero_piercing_energy'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='teleport',
            field=models.BooleanField(default=False),
        ),
    ]