# Generated by Django 5.1.2 on 2024-11-30 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_alter_appointment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]