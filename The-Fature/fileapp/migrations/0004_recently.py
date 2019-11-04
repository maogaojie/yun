# Generated by Django 2.0.4 on 2019-11-04 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
        ('fileapp', '0003_auto_20191104_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recently',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('operation', models.CharField(max_length=255)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.User')),
            ],
            options={
                'db_table': 'Recently',
            },
        ),
    ]