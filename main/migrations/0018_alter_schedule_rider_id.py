# Generated by Django 5.0.3 on 2024-04-26 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_schedule_rider_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='rider_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
