# Generated by Django 5.0.6 on 2024-06-08 20:53

import appAUDITAI.models
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAUDITAI', '0113_remove_app_list_application_owner_app_owners'),
    ]

    operations = [
        migrations.CreateModel(
            name='RF_EVIDENCE',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file_name', models.FileField(max_length=256, upload_to=appAUDITAI.models.oe_evidence_folder)),
                ('APP_NAME', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.app_list')),
                ('COMPANY_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.company')),
                ('CONTROL_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.controllist')),
            ],
            options={
                'db_table': 'RF_EVIDENCE',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='RF_TESTING',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('CONTROL_TYPE', models.CharField(blank=True, max_length=25, null=True)),
                ('CONTROL_RATING', models.CharField(blank=True, max_length=10, null=True)),
                ('CONTROL_RATING_RATIONALE', models.CharField(blank=True, max_length=500, null=True)),
                ('CONTROL_TEST_PROCEDURE', models.TextField(blank=True, null=True)),
                ('CONTROL_TEST_RESULT', models.TextField(blank=True, null=True)),
                ('CONTROL_CONCLUSION', models.CharField(blank=True, max_length=25, null=True)),
                ('CONTROL_CONCLUSION_RATIONALE', models.TextField(blank=True, null=True)),
                ('PERIOD_START_DATE', models.DateField(blank=True, null=True)),
                ('PERIOD_END_DATE', models.DateField(blank=True, null=True)),
                ('CONTROL_FREQUENCY', models.CharField(blank=True, max_length=25, null=True)),
                ('CONTROL_POPULATION', models.CharField(blank=True, max_length=25, null=True)),
                ('CONTROL_SAMPLES', models.CharField(blank=True, max_length=25, null=True)),
                ('CREATED_BY', models.CharField(blank=True, max_length=50, null=True)),
                ('CREATED_ON', models.DateField(auto_now_add=True, null=True)),
                ('LAST_MODIFIED', models.DateTimeField(null=True)),
                ('MODIFIED_BY', models.CharField(default=False, max_length=50, null=True)),
                ('APP_NAME', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.app_list')),
                ('COMPANY_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.company')),
                ('CONTROL_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.controllist')),
            ],
            options={
                'db_table': 'RF_TESTING',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='SAP_AGR_USERS',
        ),
        migrations.DeleteModel(
            name='SAP_USR02',
        ),
    ]
