# Generated by Django 5.1.3 on 2024-12-02 18:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='cat',
            constraint=models.UniqueConstraint(fields=('name', 'owner'), name='unique_name_owner'),
        ),
    ]
