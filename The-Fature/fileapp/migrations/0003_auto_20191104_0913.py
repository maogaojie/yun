# Generated by Django 2.0.4 on 2019-11-04 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileapp', '0002_auto_20191104_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liked',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='收藏状态'),
        ),
    ]
