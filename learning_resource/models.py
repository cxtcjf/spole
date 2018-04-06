from django.db import models
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField#引入ckeditor的特有类型
from ckeditor_uploader.fields import RichTextUploadingField#引入ckeditor_uploader的特有类型
# Create your models here.

'''注意：每个小组仅创建自己的一个对象即可'''

'''第一组'''
 # 创建Article对象
class ResArticle(models.Model):
    title = models.CharField(max_length=300,verbose_name='文本标题') # 创建“标题”属性，类型为字符型，长度300！
    #content = models.TextField(verbose_name='文本内容') # 创建“内容”属性，类型为大文本型，可保存的字数非常多
    #content = RichTextField(verbose_name='文本内容')#引入ckeditor编辑器
    content = RichTextUploadingField(verbose_name='文本内容')#开启ckeditor编辑器文件上传
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="res_articles",default=None,verbose_name='创建者')#外键型字段
    created = models.DateTimeField(auto_now_add=True)#日期时间型字段

    def __str__(self): #双下划线的都是类的特殊方法，这一段可不写！
        return self.title#，__str__用途是当print article的时候，会返回标题
        #而不是一串代表对象代码的数字，这样比较友好，也便于调试。
    class Meta:
        verbose_name_plural = '文本资源'#定义对象的中文别名，用于admin显示

'''第二组'''
# 创建ResPicture对象
class ResPicture(models.Model):
    title = models.CharField(max_length=300,verbose_name='图片标题') 
    #path = models.CharField(max_length=300,verbose_name='图片路径')   # 创建“路径”属性，长度300足够了
    path = models.FileField(verbose_name='图片文件')#修改为文件字段类型
    '''字段author规定了图片资源和用户之间的关系，一个用户对应多个资源
    使用ResPicture.author可以查询到创建这个资源的user
    related_name="res_pictures"的作用是，
    允许使用user.res_pictures反向查询到这个用户创建的所有图片资源
    on_delete=models.CASCADE指的是级联删除，
    也就是主表User中某个用户被删除的时候，他创建的资源也会自动删除'''
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="res_pictures",default=None,verbose_name='创建者')#外键型字段
    '''自动获取当前时间'''
    created = models.DateTimeField(auto_now_add=True)#日期时间型字段

    def __str__(self): 
        return self.title
    class Meta:
        verbose_name_plural = '图片资源'

'''第三组'''
# 创建ResDocument对象
class ResDocument(models.Model):
    title = models.CharField(max_length=300,verbose_name='标题')
    #path = models.CharField(max_length=300)
    path = models.FileField(verbose_name='文件')#修改为文件字段类型
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="res_documents",default=None,verbose_name='创建者')#外键型字段
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.title
    class Meta:
        verbose_name_plural = '文档资源'

'''第四组'''
# 创建ResAudio对象
class ResAudio(models.Model):
    title = models.CharField(max_length=300,verbose_name='标题') 
    #path = models.CharField(max_length=300)
    path = models.FileField(verbose_name='音频文件')#修改为文件字段类型
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="res_audios",default=None)#外键型字段
    created = models.DateTimeField(auto_now_add=True)#日期时间型字段

    def __str__(self): 
        return self.title
    class Meta:
        verbose_name_plural = '音频资源'

'''第五组'''
# 创建ResVideo对象
class ResVideo(models.Model):
    title = models.CharField(max_length=300,verbose_name='标题') 
    #path = models.CharField(max_length=300)
    path = models.FileField(verbose_name='视频文件')#修改为文件字段类型
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="res_videos",default=None)#外键型字段
    created = models.DateTimeField(auto_now_add=True)#日期时间型字段

    def __str__(self): 
        return self.title
    class Meta:
        verbose_name_plural = '视频资源'

'''第六组'''
# 创建ResLink对象
class ResLink(models.Model):
    title = models.CharField(max_length=300,verbose_name='标题') 
    url = models.CharField(max_length=300,verbose_name='URL')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="res_links",default=None,verbose_name='创建者')
    created = models.DateTimeField(auto_now_add=True)#日期时间型字段

    def __str__(self): 
        return self.title
    class Meta:
        verbose_name_plural = '链接资源'