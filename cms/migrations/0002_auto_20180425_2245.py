# Generated by Django 2.0.4 on 2018-04-25 14:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='introduction',
            field=ckeditor.fields.RichTextField(verbose_name='课程简介'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='内容'),
        ),
    ]