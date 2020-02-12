# Generated by Django 3.0.3 on 2020-02-12 14:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GhostPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_score', models.IntegerField(db_index=True, default=0)),
                ('num_vote_up', models.PositiveIntegerField(db_index=True, default=0)),
                ('num_vote_down', models.PositiveIntegerField(db_index=True, default=0)),
                ('body', models.CharField(max_length=280)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('boast', models.BooleanField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
