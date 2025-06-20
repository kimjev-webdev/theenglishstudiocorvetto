# Generated by Django 5.2.1 on 2025-06-07 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Class Name')),
                ('emoji', models.CharField(help_text='Use a single emoji to represent this class', max_length=10, verbose_name='Emoji')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('class_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.class', verbose_name='Class')),
            ],
        ),
    ]
