# Generated by Django 5.1 on 2024-09-10 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='coins',
            field=models.IntegerField(default=0),
        ),
    ]
