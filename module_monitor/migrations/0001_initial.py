# Generated by Django 2.1.2 on 2018-12-12 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_execution', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(blank=True, null=True)),
                ('interval_minutes', models.IntegerField(default=10)),
            ],
        ),
    ]
