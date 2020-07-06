# Generated by Django 3.0.6 on 2020-06-12 08:58
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_blogdetailpage_categories"),
    ]

    operations = [
        migrations.RemoveField(model_name="blogdetailpage", name="categories",),
        migrations.AddField(
            model_name="blogdetailpage",
            name="categories",
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to="blog.BlogCategory"),
            preserve_default=False,
        ),
    ]
