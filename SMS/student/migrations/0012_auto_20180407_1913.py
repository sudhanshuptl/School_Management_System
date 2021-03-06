# Generated by Django 2.0.3 on 2018-04-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20180407_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentenroll',
            name='enroll_date',
            field=models.DateField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='studentenroll',
            name='roll_num',
            field=models.CharField(db_index=True, help_text='Assign Roll Number formate : YY+class_code+max_seq', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='studentenroll',
            unique_together={('student', 'section')},
        ),
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['last_name', 'first_name'], name='student_stu_last_na_81e726_idx'),
        ),
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['first_name'], name='first_name_idx'),
        ),
    ]
