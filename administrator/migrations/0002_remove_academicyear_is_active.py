# Generated by Django 5.0.1 on 2025-02-05 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicyear',
            name='is_active',
        ),
    ]
