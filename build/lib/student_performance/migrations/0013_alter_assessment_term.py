# Generated by Django 5.0.1 on 2024-04-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_performance', '0012_assessment_class_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='term',
            field=models.CharField(choices=[('1st Semester', 'Semester 1'), ('2nd Semester', 'Semester 2')], max_length=50),
        ),
    ]
