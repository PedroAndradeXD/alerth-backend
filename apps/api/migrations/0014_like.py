# Generated by Django 5.1.1 on 2024-11-23 19:28

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_client_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('like_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.client')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.event')),
            ],
            options={
                'unique_together': {('client', 'event')},
            },
        ),
    ]
