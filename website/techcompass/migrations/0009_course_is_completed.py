# Generated by Django 5.1.2 on 2024-12-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techcompass', '0008_alter_roadmap_badge_alter_roadmap_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
