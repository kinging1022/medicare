# Generated by Django 5.1.2 on 2024-11-03 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_alter_appointment_options_appointment_created_for_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('sent', 'Sent'), ('processed', 'Processed'), ('done', 'Done')], default='sent', max_length=50),
        ),
    ]