# Generated by Django 2.0.3 on 2018-04-26 10:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ApiManager', '0005_envinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='envinfo',
            name='env_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='envinfo',
            name='base_url',
            field=models.CharField(max_length=40),
        ),
    ]
