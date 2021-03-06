# Generated by Django 2.0.3 on 2018-04-06 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning_resource', '0005_auto_20180328_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='resaudio',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='res_audios', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='resaudio',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resvideo',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='res_videos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='resvideo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resaudio',
            name='path',
            field=models.FileField(upload_to='', verbose_name='音频文件'),
        ),
        migrations.AlterField(
            model_name='reslink',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='res_links', to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
        ),
        migrations.AlterField(
            model_name='respicture',
            name='path',
            field=models.FileField(upload_to='', verbose_name='图片文件'),
        ),
        migrations.AlterField(
            model_name='resvideo',
            name='path',
            field=models.FileField(upload_to='', verbose_name='视频文件'),
        ),
    ]
