# Generated by Django 3.0.6 on 2020-06-12 08:59
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_auto_20200612_0858"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogdetailpage",
            name="categories",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="blog.BlogCategory"),
        ),
    ]