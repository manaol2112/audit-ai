# Generated by Django 4.2.11 on 2024-04-28 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appAUDITAI', '0053_app_job_pull_friday_app_job_pull_monday_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='USER_LOCKOUT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('failed_attempts', models.IntegerField(default=0)),
                ('locked_out', models.BooleanField(default=False)),
                ('last_attempt_timestamp', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
