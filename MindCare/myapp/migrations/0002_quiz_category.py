# Generated by Django 5.1.2 on 2025-02-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='category',
            field=models.CharField(default='General', max_length=100),
        ),
    ]
