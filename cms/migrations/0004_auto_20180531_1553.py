# Generated by Django 2.0.4 on 2018-05-31 07:53

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20180426_1139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='completion',
            old_name='complate_at',
            new_name='complete_at',
        ),
        migrations.AlterField(
            model_name='completion',
            name='member',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='completions', to='cms.Member', verbose_name='学生'),
        ),
        migrations.AlterField(
            model_name='completion',
            name='syllabus',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='completions', to='cms.Syllabus', verbose_name='大纲节点'),
        ),
        migrations.AlterField(
            model_name='course',
            name='introduction',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='课程简介'),
        ),
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(choices=[('teacher', '教师'), ('student', '学生')], max_length=300, verbose_name='角色'),
        ),
        migrations.AlterField(
            model_name='question',
            name='qtype',
            field=models.CharField(choices=[('single', '单选题'), ('multiple', '多选题'), ('judgment', '判断题')], max_length=300, verbose_name='题型'),
        ),
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='题干'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容'),
        ),
    ]
