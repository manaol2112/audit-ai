# Generated by Django 5.0.4 on 2024-04-22 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAUDITAI', '0031_password_auth_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='app_list',
            name='SETUP_COMPLETE',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]