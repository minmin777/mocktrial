# Generated by Django 2.0.7 on 2018-08-24 13:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MockTrial', '0008_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitational',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='MainLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
