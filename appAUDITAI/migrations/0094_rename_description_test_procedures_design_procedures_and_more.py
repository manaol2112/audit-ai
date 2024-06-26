# Generated by Django 5.0.6 on 2024-06-02 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAUDITAI', '0093_test_procedures_phase_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test_procedures',
            old_name='DESCRIPTION',
            new_name='DESIGN_PROCEDURES',
        ),
        migrations.RemoveField(
            model_name='test_procedures',
            name='PHASE',
        ),
        migrations.AddField(
            model_name='test_procedures',
            name='INTERIM_PROCEDURES',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='test_procedures',
            name='ROLLFORWARD_PROCEDURES',
            field=models.TextField(blank=True, null=True),
        ),
    ]
