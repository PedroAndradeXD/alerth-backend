# Generated by Django 5.1.1 on 2024-11-21 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_event_service_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
