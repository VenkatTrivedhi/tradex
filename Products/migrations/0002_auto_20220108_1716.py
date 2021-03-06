# Generated by Django 3.2.6 on 2022-01-08 11:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='password',
        ),
        migrations.RemoveField(
            model_name='products',
            name='username',
        ),
        migrations.AddField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
