# Generated by Django 5.1.5 on 2025-02-03 21:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='datecompleted',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='important',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
