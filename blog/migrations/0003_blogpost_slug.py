# Generated by Django 2.2 on 2020-02-18 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='Hello-world'),
            preserve_default=False,
        ),
    ]
