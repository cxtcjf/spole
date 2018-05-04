from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField#引入ckeditor的特有类型

# Create your models here.
#课程模型
class Course(models.Model):
    name = models.CharField(max_length=300,verbose_name='课程名称')
    code = models.CharField(max_length=300,verbose_name='课程代码')
    #introduction = models.TextField(verbose_name='课程简介')
    introduction = RichTextField(verbose_name='课程简介')#引入ckeditor编辑器
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
    #content = models.TextField(verbose_name='内容')
    content = RichTextField(verbose_name='内容')#引入ckeditor编辑器
    author = models.ForeignKey(User,on_delete=models.SET_NULL,related_name="syllabuses",null=True,blank=True,default=None,verbose_name='创建者')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.title
    class Meta:
        verbose_name_plural = '大纲'


#课程成员模型
class Member(models.Model):
    ROLE_CHOICES = (
    ('teacher', '教师'),
    ('student', '学生'),
    )
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="members",default=None,verbose_name='所属课程')
    name = models.CharField(max_length=300,verbose_name='姓名')
    sno = models.CharField(max_length=300,verbose_name='学号')
    user = models.ForeignKey(User,on_delete=models.SET_NULL,related_name="members",null=True,blank=True,default=None,verbose_name='系统用户')
    role = models.CharField(max_length=300,choices=ROLE_CHOICES,verbose_name='角色')
    joined = models.DateTimeField(auto_now_add=True,verbose_name='加入时间')

    def __str__(self): 
        return self.name
    class Meta:
        verbose_name_plural = '成员'

#教学进度模型
class Completion(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="completions",default=None,verbose_name='所属课程')
    syllabus = models.ForeignKey(Syllabus,on_delete=models.CASCADE,related_name="completions",default=None,verbose_name='大纲节点')
    member = models.ForeignKey(Member,on_delete=models.CASCADE,related_name="completions",default=None,verbose_name='学生')
    complete = models.BooleanField(verbose_name='完成情况')
    complete_at = models.DateTimeField(auto_now=True,verbose_name='记录时间')

    def __str__(self): 
        return self.course.name+'-'+self.syllabus.title+'('+self.syllabus.level+')-'+self.member.name
    class Meta:
        verbose_name_plural = '进度'



#成绩模型
class Grade(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="grades",default=None,verbose_name='所属课程')
    member = models.ForeignKey(Member,on_delete=models.CASCADE,related_name="grades",default=None,verbose_name='学生')
    item = models.CharField(max_length=300,verbose_name='成绩项')
    score = models.CharField(max_length=300,verbose_name='得分')
    grader = models.CharField(max_length=300,verbose_name='评分人')
   
    def __str__(self): 
        return self.course+'-'+self.member+'-'+self.item
    class Meta:
        verbose_name_plural = '成绩'

#题目模型
class Question(models.Model):
    QTYPE_CHOICES = (
    ('single', '单选题'),
    ('multiple', '多选题'),
    ('judgment', '判断题'),
    )
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="questions",default=None,verbose_name='所属课程')
    title = models.CharField(max_length=300,verbose_name='标题')
    subject = RichTextField(verbose_name='题干')
    qtype = models.CharField(max_length=300,choices=QTYPE_CHOICES,verbose_name='题型')
    score = models.CharField(max_length=300,verbose_name='得分')
    
    def __str__(self): 
        return self.title
    class Meta:
        verbose_name_plural = '题目'

class Option(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name="options",default=None,verbose_name='所属题目')
    content = models.CharField(max_length=300,verbose_name='选项内容')
    correct = models.BooleanField(verbose_name='是否答案')

    def __str__(self): 
        return self.content
    class Meta:
        verbose_name_plural = '题目选项'