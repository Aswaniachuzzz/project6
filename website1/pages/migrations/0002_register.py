# Generated by Django 5.0.2 on 2024-02-14 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_name', models.CharField(max_length=255)),
                ('reg_email', models.EmailField(max_length=255)),
                ('reg_phnnumber', models.CharField(max_length=255)),
                ('reg_username', models.CharField(max_length=255)),
                ('reg_password', models.CharField(max_length=255)),
            ],
        ),
    ]
