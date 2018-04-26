# Generated by Django 2.0.3 on 2018-04-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiManager', '0004_auto_20180424_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('base_url', models.CharField(max_length=50)),
                ('simple_desc', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'EnvInfo',
                'verbose_name': '环境管理',
            },
        ),
    ]
