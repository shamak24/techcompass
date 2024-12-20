# Generated by Django 5.1.3 on 2024-12-12 17:31

import techcompass.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techcompass', '0007_roadmap_badge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roadmap',
            name='badge',
            field=models.FileField(blank=True, null=True, upload_to='badges/', validators=[techcompass.models.validate_svg]),
        ),
        migrations.AlterField(
            model_name='roadmap',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
