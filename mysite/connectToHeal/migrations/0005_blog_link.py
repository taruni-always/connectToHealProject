# Generated by Django 3.2.7 on 2021-12-12 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connectToHeal', '0004_blog_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='link',
            field=models.URLField(default=''),
        ),
    ]