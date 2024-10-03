# Generated by Django 5.1.1 on 2024-09-10 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='coin',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('student', 'student'), ('teacher', 'teacher')], default='student', max_length=10),
        ),
    ]