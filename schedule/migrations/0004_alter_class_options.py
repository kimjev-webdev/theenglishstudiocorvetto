# Generated by Django 5.2.1 on 2025-06-08 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_remove_event_time_event_end_time_event_start_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name': 'Class', 'verbose_name_plural': 'Classes'},
        ),
    ]
