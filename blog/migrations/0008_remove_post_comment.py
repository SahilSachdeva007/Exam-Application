# Generated by Django 4.0.5 on 2023-03-03 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
    ]
