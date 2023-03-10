# Generated by Django 4.1.2 on 2022-11-19 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0003_alter_item_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.CharField(
                choices=[
                    ("K", "Kits"),
                    ("B", "Balls"),
                    ("A", "Accessories"),
                    ("F", "Footwear"),
                ],
                max_length=2,
            ),
        ),
        migrations.CreateModel(
            name="CheckoutAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("street_address", models.CharField(max_length=100)),
                ("apartment_address", models.CharField(max_length=100)),
                ("country", django_countries.fields.CountryField(max_length=2)),
                ("zip", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
