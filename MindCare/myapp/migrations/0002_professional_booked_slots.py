# Generated by Django 5.1.2 on 2025-02-11 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professional',
            name='booked_slots',
            field=models.JSONField(default=list),
        ),
    ]
