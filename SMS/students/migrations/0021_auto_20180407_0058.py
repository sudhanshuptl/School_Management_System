# Generated by Django 2.0.3 on 2018-04-06 19:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0020_auto_20180407_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classteacher',
            name='staff',
            field=models.ForeignKey(db_column='user_name', on_delete=django.db.models.deletion.PROTECT, to='students.Staff', unique=True),
        ),
        migrations.AlterField(
            model_name='studentattendance',
            name='Attend_date',
            field=models.DateField(blank=True, db_index=True, default=datetime.datetime(2018, 4, 7, 0, 58, 47, 835018)),
        ),
    ]