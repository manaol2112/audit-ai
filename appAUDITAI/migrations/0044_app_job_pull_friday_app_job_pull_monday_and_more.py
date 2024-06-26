# Generated by Django 5.0.4 on 2024-04-25 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAUDITAI', '0043_app_job_pull_friday_app_job_pull_monday_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='APP_JOB_USER_LOG_PROCESS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USER_ID', models.CharField(blank=True, max_length=128, null=True)),
                ('JOB_DATE', models.DateTimeField(null=True)),
                ('JOB_FILE_DESTINATION', models.CharField(blank=True, max_length=1000, null=True)),
                ('JOB_ERROR', models.CharField(blank=True, max_length=1000, null=True)),
                ('JOB_COMPLETE', models.BooleanField(default=False, null=True)),
                ('APP_NAME', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.app_list')),
            ],
            options={
                'db_table': 'APP_JOB_USER_LOG_PROCESS',
                'managed': True,
            },
        ),
    ]
