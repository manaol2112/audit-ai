# Generated by Django 5.0.6 on 2024-06-02 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appAUDITAI', '0095_alter_test_procedures_control_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test_procedures',
            name='CONTROL_ID',
        ),
    ]