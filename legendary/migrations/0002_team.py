# Generated by Django 2.0.3 on 2018-03-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legendary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
