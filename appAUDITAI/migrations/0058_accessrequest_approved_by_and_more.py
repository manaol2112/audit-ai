# Generated by Django 5.0.4 on 2024-05-07 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAUDITAI', '0057_accessrequest_accessrequestcomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessrequest',
            name='APPROVED_BY',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='accessrequest',
            name='LAST_MODIFIED',
            field=models.DateTimeField(null=True),
        ),
    ]
