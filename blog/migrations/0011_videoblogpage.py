# Generated by Django 3.0.6 on 2020-06-23 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_articleblogpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoBlogPage',
            fields=[
                ('blogdetailpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.BlogDetailPage')),
                ('youtube_video_id', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('blog.blogdetailpage',),
        ),
    ]
