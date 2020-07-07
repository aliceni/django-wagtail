# Generated by Django 3.0.6 on 2020-06-08 02:40
import django.db.models.deletion
from django.db import migrations, models

import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks

import streams.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailimages", "0022_uploadedimage"),
        ("wagtailcore", "0045_assign_unlock_grouppagepermission"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogListingPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                ("custom_title", models.CharField(help_text="Overwrites the default title", max_length=100)),
            ],
            options={"verbose_name": "Blog Listing Page", "verbose_name_plural": "Blog Listing Pages",},
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="BlogDetailPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                ("custom_title", models.CharField(help_text="Overwrites the default title", max_length=100)),
                (
                    "content",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "title_and_text",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        (
                                            "title",
                                            wagtail.core.blocks.CharBlock(help_text="Add your title", required=True),
                                        ),
                                        (
                                            "text",
                                            wagtail.core.blocks.TextBlock(
                                                help_text="Add additional text", required=True
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            ("full_richtext", streams.blocks.RichtextBlock()),
                            ("simple_richtext", streams.blocks.SimpleRichtextBlock()),
                            (
                                "cards",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        (
                                            "title",
                                            wagtail.core.blocks.CharBlock(help_text="Add your title", required=True),
                                        ),
                                        (
                                            "cards",
                                            wagtail.core.blocks.ListBlock(
                                                wagtail.core.blocks.StructBlock(
                                                    [
                                                        (
                                                            "image",
                                                            wagtail.images.blocks.ImageChooserBlock(required=True),
                                                        ),
                                                        (
                                                            "title",
                                                            wagtail.core.blocks.CharBlock(max_length=40, required=True),
                                                        ),
                                                        (
                                                            "text",
                                                            wagtail.core.blocks.TextBlock(
                                                                max_length=200, required=True
                                                            ),
                                                        ),
                                                        (
                                                            "button_page",
                                                            wagtail.core.blocks.PageChooserBlock(required=False),
                                                        ),
                                                        (
                                                            "button_url",
                                                            wagtail.core.blocks.URLBlock(
                                                                help_text="If the button page above is selected, then use it first.",
                                                                required=False,
                                                            ),
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "cta",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        ("title", wagtail.core.blocks.CharBlock(max_length=60, required=True)),
                                        (
                                            "text",
                                            wagtail.core.blocks.RichTextBlock(
                                                features=["bold", "italic"], required=True
                                            ),
                                        ),
                                        ("button_page", wagtail.core.blocks.PageChooserBlock(required=False)),
                                        ("button_url", wagtail.core.blocks.URLBlock(required=False)),
                                        (
                                            "button_text",
                                            wagtail.core.blocks.CharBlock(
                                                default="Learn More", max_length=40, required=True
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                        ],
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "blog_image",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                    ),
                ),
            ],
            options={"verbose_name": "Blog Detail Page", "verbose_name_plural": "Blog Detail Pages",},
            bases=("wagtailcore.page",),
        ),
    ]