# Generated by Django 2.0.3 on 2018-03-19 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('legendary', '0011_auto_20180319_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legendary.Team'),
        ),
    ]