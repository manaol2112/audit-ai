# Generated by Django 5.0.4 on 2024-04-22 22:43

import appAUDITAI.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAUDITAI', '0033_password_setup_complete_alter_app_list_modified_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='APP_JOB_PULL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JOB_NAME', models.CharField(blank=True, max_length=1000, null=True)),
                ('SCHEDULE_TIME', models.TimeField()),
                ('CREATED_BY', models.CharField(blank=True, max_length=50, null=True)),
                ('CREATED_ON', models.DateField(auto_now_add=True, null=True)),
                ('LAST_MODIFIED', models.DateTimeField(null=True)),
                ('MODIFIED_BY', models.CharField(blank=True, max_length=50, null=True)),
                ('APP_NAME', models.ForeignKey(blank=True, max_length=100, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.app_list')),
            ],
            options={
                'db_table': 'USER_JOB_SCHEDULE',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='APP_JOB_USER_LOG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JOB_COMPLETE', models.BooleanField(default=False)),
                ('JOB_NAME', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appAUDITAI.app_job_pull')),
            ],
            options={
                'db_table': 'APP_JOB_USER_LOG',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='APP_USER_SFTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HOST_NAME', models.CharField(blank=True, max_length=1000, null=True)),
                ('SFTP_PW_HASHED', models.CharField(blank=True, max_length=128, null=True)),
                ('SFTP_DIRECTORY', models.CharField(blank=True, max_length=1000, null=True)),
                ('SFTP_DESTINATION', models.CharField(blank=True, max_length=1000, null=True)),
                ('CREATED_BY', models.CharField(blank=True, max_length=50, null=True)),
                ('CREATED_ON', models.DateField(auto_now_add=True, null=True)),
                ('LAST_MODIFIED', models.DateTimeField(null=True)),
                ('MODIFIED_BY', models.CharField(blank=True, max_length=50, null=True)),
                ('APP_NAME', models.ForeignKey(blank=True, max_length=100, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.app_list')),
            ],
            options={
                'db_table': 'SFTP_USER',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HR_JOB_PULL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JOB_NAME', models.CharField(blank=True, max_length=1000, null=True)),
                ('SCHEDULE_TIME', models.TimeField()),
                ('CREATED_BY', models.CharField(blank=True, max_length=50, null=True)),
                ('CREATED_ON', models.DateField(auto_now_add=True, null=True)),
                ('LAST_MODIFIED', models.DateTimeField(null=True)),
                ('MODIFIED_BY', models.CharField(blank=True, max_length=50, null=True)),
                ('COMPANY_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.company')),
            ],
            options={
                'db_table': 'HR_JOB_SCHEDULE',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HR_JOB_USER_LOG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JOB_COMPLETE', models.BooleanField(default=False)),
                ('JOB_NAME', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appAUDITAI.app_job_pull')),
            ],
            options={
                'db_table': 'HR_JOB_USER_LOG',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HR_LIST_SFTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HOST_NAME', models.CharField(blank=True, max_length=1000, null=True)),
                ('SFTP_PW_HASHED', models.CharField(blank=True, max_length=128, null=True)),
                ('SFTP_DIRECTORY', models.CharField(blank=True, max_length=1000, null=True)),
                ('SFTP_DESTINATION', models.CharField(blank=True, max_length=1000, null=True)),
                ('CREATED_BY', models.CharField(blank=True, max_length=50, null=True)),
                ('CREATED_ON', models.DateField(auto_now_add=True, null=True)),
                ('LAST_MODIFIED', models.DateTimeField(null=True)),
                ('MODIFIED_BY', models.CharField(blank=True, max_length=50, null=True)),
                ('COMPANY_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.company')),
            ],
            options={
                'db_table': 'SFTP_HR',
                'managed': True,
            },
        ),
    ]
