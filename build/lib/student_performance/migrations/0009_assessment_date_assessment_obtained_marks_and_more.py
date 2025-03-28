# Generated by Django 5.0.1 on 2024-04-02 17:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_performance', '0008_alter_classenrollment_academic_year'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assessment',
            name='obtained_marks',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='assessment',
            name='student',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='student_performance.student'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='teacher',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='student_assessment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='AssessmentResult',
        ),
    ]
