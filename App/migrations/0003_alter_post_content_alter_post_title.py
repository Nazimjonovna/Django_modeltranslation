# Generated by Django 5.1 on 2024-08-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
    ]
