# Generated by Django 2.2.6 on 2020-04-08 23:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lat', models.DecimalField(decimal_places=16, max_digits=20)),
                ('long', models.DecimalField(decimal_places=16, max_digits=20)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracking_unit', to='units.Unit')),
            ],
        ),
    ]
