# Generated by Django 5.0.3 on 2024-04-01 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_user_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='persons',
            field=models.ImageField(blank=True, default='static/image/icon/profile.png', null=True, upload_to='static/image'),
        ),
    ]
