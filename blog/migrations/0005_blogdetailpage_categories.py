# Generated by Django 3.0.6 on 2020-06-12 08:34
from django.db import migrations

import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_blogcategory"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogdetailpage",
            name="categories",
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to="blog.BlogCategory"),
        ),
    ]
