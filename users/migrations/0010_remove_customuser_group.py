# Generated by Django 5.1 on 2024-09-12 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_customuser_group_alter_group_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='group',
        ),
    ]