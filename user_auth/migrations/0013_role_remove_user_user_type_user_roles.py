# Generated by Django 5.0.1 on 2024-12-23 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0012_alter_user_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(related_name='users', to='user_auth.role'),
        ),
    ]
