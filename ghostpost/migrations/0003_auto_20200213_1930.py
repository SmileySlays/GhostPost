# Generated by Django 3.0.3 on 2020-02-13 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost', '0002_remove_ghostpost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ghostpost',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]