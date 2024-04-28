# Generated by Django 5.0.3 on 2024-04-28 16:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('isRider', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.CharField(blank=True, max_length=50, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_id', models.CharField(blank=True, max_length=20, null=True)),
                ('pickUp_time', models.CharField(max_length=10)),
                ('pickup_from', models.CharField(max_length=50)),
                ('drop_to', models.CharField(max_length=50)),
                ('pending', models.BooleanField(default=True)),
                ('type_of_schedule', models.CharField(blank=True, choices=[('daily', 'daily'), ('weekly', 'weekly'), ('monthly', 'monthly'), ('custom', 'custom')], max_length=10, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('startDate', models.CharField(blank=True, max_length=30, null=True)),
                ('endDate', models.CharField(blank=True, max_length=30, null=True)),
                ('weeks', models.CharField(blank=True, max_length=30, null=True)),
                ('rider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
    ]
