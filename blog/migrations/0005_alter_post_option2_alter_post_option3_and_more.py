# Generated by Django 4.0.5 on 2023-03-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_views_alter_post_option1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='option2',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='post',
            name='option3',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='post',
            name='option4',
            field=models.CharField(max_length=55),
        ),
    ]
