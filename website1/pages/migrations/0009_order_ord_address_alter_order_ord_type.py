# Generated by Django 5.0.2 on 2024-03-07 07:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0008_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="ord_address",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="ord_type",
            field=models.CharField(max_length=10, null=True),
        ),
    ]
