# Generated by Django 2.0.7 on 2018-08-19 17:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MockTrial', '0007_auto_20180819_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', ckeditor.fields.RichTextField()),
            ],
        ),
    ]