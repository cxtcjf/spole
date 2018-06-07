from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
#作业模型
class Assignment(models.Model):
    SCORE_TYPE_CHOICES = (
    ('scale', '评级'),
    ('point', '评分'),
    )
    code = models.CharField(max_length=300,verbose_name='代码')
    title = models.CharField(max_length=300,verbose_name='作业名称')
    description = RichTextUploadingField(blank=True,verbose_name='作业描述')
    attachment = models.FileField(blank=True,verbose_name='附件')#文件字段类型
    begin = models.DateTimeField(verbose_name='开始时间')
    end = models.DateTimeField(verbose_name='截止时间')
    score_type = models.CharField(max_length=300,choices=SCORE_TYPE_CHOICES,verbose_name='作业类型')
    pass_line = models.CharField(max_length=300,verbose_name='及格线')

    def __str__(self): 
        return self.title
    class Meta:
        verbose_name_plural = '作业'

#作业结果模型
class Solution(models.Model):
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE,related_name="solutions",default=None,verbose_name='所属作业')
    sno = models.CharField(max_length=300,verbose_name='学号')
    name = models.CharField(max_length=300,verbose_name='姓名')
    content = RichTextUploadingField(blank=True,verbose_name='作业内容')
    attachment = models.FileField(blank=True,verbose_name='附件')#文件字段类型
    created = models.DateTimeField(auto_now_add=True,verbose_name='提交时间')
    score = models.CharField(blank=True,max_length=300,verbose_name='得分')
    correction = RichTextUploadingField(blank=True,verbose_name='批改')

    def __str__(self): 
        return self.assignment.code+'-'+self.sno
    class Meta:
        verbose_name_plural = '作业结果'