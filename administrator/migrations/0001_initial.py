# Generated by Django 5.0.1 on 2025-02-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-start_year'],
            },
        ),
    ]
