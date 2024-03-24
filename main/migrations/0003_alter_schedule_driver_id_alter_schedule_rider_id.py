# Generated by Django 5.0.3 on 2024-03-24 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_driver_rider_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='driver_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.driver'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='rider_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.rider'),
        ),
    ]