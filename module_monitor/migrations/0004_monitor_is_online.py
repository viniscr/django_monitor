# Generated by Django 2.1.2 on 2018-12-12 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_monitor', '0003_monitor_status_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='is_online',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
