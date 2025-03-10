# Generated by Django 5.0.1 on 2024-10-10 12:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_performance', '0028_teacherlevelclass_is_main_teacher'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetables', to='student_performance.class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_performance.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
