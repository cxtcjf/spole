from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#课程模型
class Course(models.Model):
    name = models.CharField(max_length=300,verbose_name='课程名称')
    code = models.CharField(max_length=300,verbose_name='课程代码')
    introduction = models.TextField(verbose_name='课程简介')
    picture = models.ImageField(verbose_name='课程封面')
    term = models.CharField(max_length=300,verbose_name='学期代码')
    author = models.ForeignKey(User,on_delete=models.CASCADE,\
      related_name="courses",default=None,verbose_name='创建者')#外键型字段
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name
    class Meta:
        verbose_name_plural = '课程'


#教学大纲模型
class Syllabus(models.Model):
    LEVEL_CHOICES = (
    ('chapter', '章'),
    ('section', '节'),
    ('unit', '单元'),
    )
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="syllabuses",default=None,verbose_name='所属课程')
    title = models.CharField(max_length=300,verbose_name='标题') 
    level = models.CharField(max_length=7,choices=LEVEL_CHOICES,verbose_name='层次类型')
    parent = models.ForeignKey('self',on_delete=models.PROTECT,related_name="children",null=True,blank=True,default=None,verbose_name='上级节点') 
    content = models.TextField(verbose_name='内容')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,related_name="syllabuses",null=True,blank=True,default=None,verbose_name='创建者')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.title
    class Meta:
        verbose_name_plural = '大纲'