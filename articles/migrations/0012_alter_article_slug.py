# Generated by Django 3.2.15 on 2022-09-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]