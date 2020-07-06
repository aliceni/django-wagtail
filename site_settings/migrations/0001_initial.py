# Generated by Django 3.0.6 on 2020-05-25 08:14
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0045_assign_unlock_grouppagepermission"),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialMediaSettings",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("facebook", models.URLField(blank=True, help_text="Facebook URL", null=True)),
                ("twitter", models.URLField(blank=True, help_text="Twitter URL", null=True)),
                ("youtube", models.URLField(blank=True, help_text="Youtube Channel URL", null=True)),
                (
                    "site",
                    models.OneToOneField(
                        editable=False, on_delete=django.db.models.deletion.CASCADE, to="wagtailcore.Site"
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
