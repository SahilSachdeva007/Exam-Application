# Generated by Django 3.2.8 on 2021-12-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=14)), 
                ('slug', models.CharField(max_length=130)),
                # ('timeStamp', models.DateTimeField(blank=True)),
                ('content', models.TextField()),
                ('option1', models.CharField(max_length=15)),
                ('option2', models.CharField(max_length=15)),
                ('option3', models.CharField(max_length=15)),
                ('option4', models.CharField(max_length=15)),
                # ('comment', models.TextField(blank=True)),

            ],
        ),
    ]
