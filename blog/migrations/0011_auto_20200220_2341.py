# Generated by Django 2.2 on 2020-02-20 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
