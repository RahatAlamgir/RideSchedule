# Generated by Django 5.0.3 on 2024-03-24 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=10)),
                ('postal_Code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=11)),
            ],
        ),
    ]
