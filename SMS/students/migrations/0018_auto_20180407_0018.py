# Generated by Django 2.0.3 on 2018-04-06 18:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0017_auto_20180406_2331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjects',
            old_name='class_name',
            new_name='classes',
        ),
        migrations.RemoveField(
            model_name='classteacher',
            name='class_Teacher',
        ),
        migrations.RemoveField(
            model_name='classteacher',
            name='class_code',
        ),
        migrations.RemoveField(
            model_name='parents',
            name='Roll_Num',
        ),
        migrations.RemoveField(
            model_name='section',
            name='class_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='class_code',
        ),
        migrations.RemoveField(
            model_name='studentattendance',
            name='Roll_Num',
        ),
        migrations.RemoveField(
            model_name='studentattendance',
            name='user_entry',
        ),
        migrations.RemoveField(
            model_name='subjectenroll',
            name='Roll_Num',
        ),
        migrations.RemoveField(
            model_name='subjectenroll',
            name='subject_code',
        ),
        migrations.AddField(
            model_name='classteacher',
            name='section',
            field=models.ForeignKey(db_column='class_code', default='', on_delete=django.db.models.deletion.CASCADE, to='students.Section'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classteacher',
            name='staff',
            field=models.ForeignKey(db_column='user_name', default=' ', on_delete=django.db.models.deletion.PROTECT, to='students.Staff'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parents',
            name='student',
            field=models.ForeignKey(db_column='Roll_Num', default='', on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='classes',
            field=models.ForeignKey(db_column='class_name', default='', on_delete=django.db.models.deletion.CASCADE, to='students.Class'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='section',
            field=models.ForeignKey(db_column='class_code', default='', on_delete=django.db.models.deletion.CASCADE, to='students.Section'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='staff',
            field=models.ForeignKey(db_column='user_name', default='', on_delete=django.db.models.deletion.DO_NOTHING, to='students.Staff'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='student',
            field=models.ForeignKey(db_column='Roll_Num', default='', on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subjectenroll',
            name='students',
            field=models.ForeignKey(db_column='Roll_Num', default='', on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subjectenroll',
            name='subjects',
            field=models.ForeignKey(db_column='subject_code', default='', on_delete=django.db.models.deletion.CASCADE, to='students.Subjects'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='section',
            field=models.CharField(default='A', max_length=5),
        ),
        migrations.AlterField(
            model_name='staff',
            name='StaffType',
            field=models.ForeignKey(db_column='staff_type', on_delete=django.db.models.deletion.PROTECT, to='students.StaffType'),
        ),
        migrations.AlterField(
            model_name='studentattendance',
            name='Attend_date',
            field=models.DateField(blank=True, db_index=True, default=datetime.datetime(2018, 4, 7, 0, 16, 23, 671892)),
        ),
    ]
