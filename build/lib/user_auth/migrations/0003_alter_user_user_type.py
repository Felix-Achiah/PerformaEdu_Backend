# Generated by Django 5.0.1 on 2024-03-01 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_user_first_name_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Parent', 'Parent'), ('Headmaster', 'Headmaster'), ('Teacher', 'Teacher')], max_length=100),
        ),
    ]
