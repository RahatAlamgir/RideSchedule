# Generated by Django 5.0.3 on 2024-03-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_schedule_driver_id_remove_schedule_rider_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]