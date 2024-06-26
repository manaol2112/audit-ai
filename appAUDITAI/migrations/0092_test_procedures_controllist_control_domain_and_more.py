# Generated by Django 5.0.6 on 2024-06-01 18:08

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAUDITAI', '0091_alter_riskmapping_risk_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TEST_PROCEDURES',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('CONTROL_ID', models.CharField(blank=True, max_length=256, null=True)),
                ('TYPE', models.CharField(blank=True, max_length=256, null=True)),
                ('DESCRIPTION', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'TEST_PROCEDURE',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='controllist',
            name='CONTROL_DOMAIN',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='controllist',
            name='CONTROL_RELEVANCE',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='controllist',
            name='CONTROL_TITLE',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
