# Generated by Django 2.0.3 on 2018-03-19 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legendary', '0008_auto_20180319_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='recruitment_points',
        ),
    ]