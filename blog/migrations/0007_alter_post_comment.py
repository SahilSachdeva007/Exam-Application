# Generated by Django 4.0.5 on 2023-03-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.TextField(),
        ),
    ]