# Generated by Django 4.2.7 on 2024-02-19 06:41

import django.contrib.admin.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('firstname', models.TextField(max_length=255)),
                ('lastname', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('comments', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'contactus',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Register',
            },
        ),
        migrations.CreateModel(
            name='RentCar',
            fields=[
                ('location1', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('from_date_value', models.DateField()),
                ('to_date_value', models.DateField()),
            ],
            options={
                'db_table': 'rentcar',
            },
        ),
        migrations.CreateModel(
            name='CustomLogEntry',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('admin.logentry',),
            managers=[
                ('objects', django.contrib.admin.models.LogEntryManager()),
            ],
        ),
    ]