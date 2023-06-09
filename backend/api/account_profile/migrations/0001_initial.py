# Generated by Django 4.1.4 on 2023-04-26 03:26

import config.helpers
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AccountProfile",
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
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True,
                        upload_to=config.helpers.get_profile_photo_upload_path,
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["png", "jpg", "jpeg"]
                            )
                        ],
                        verbose_name="profile picture",
                    ),
                ),
                (
                    "website_links",
                    models.URLField(default="", verbose_name="website links"),
                ),
                ("city", models.CharField(max_length=20, verbose_name="city")),
                ("state", models.CharField(max_length=20, verbose_name="state")),
                ("country", models.CharField(max_length=20, verbose_name="country")),
                (
                    "account",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="account",
                    ),
                ),
            ],
            options={
                "verbose_name": "User Profile",
                "verbose_name_plural": "User Profiles",
            },
        ),
    ]
