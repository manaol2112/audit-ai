# Generated by Django 5.0.6 on 2024-06-02 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAUDITAI', '0096_remove_test_procedures_control_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_procedures',
            name='CONTROL_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appAUDITAI.controllist'),
        ),
    ]
