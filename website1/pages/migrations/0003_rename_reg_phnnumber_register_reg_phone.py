# Generated by Django 5.0.2 on 2024-02-14 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='reg_phnnumber',
            new_name='reg_phone',
        ),
    ]