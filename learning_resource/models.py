from django.db import models

# Create your models here.

'''注意：每个小组仅创建自己的一个对象即可'''

'''第一组'''
 # 创建Article对象
class ResArticle(models.Model):
    title = models.CharField(max_length=300,verbose_name='文本标题') # 创建“标题”属性，类型为字符型，长度300！
    content = models.TextField(verbose_name='文本内容') # 创建“内容”属性，类型为大文本型，可保存的字数非常多

    def __str__(self): #双下划线的都是类的特殊方法，这一段可不写！
        return self.title#，__str__用途是当print article的时候，会返回标题
        #而不是一串代表对象代码的数字，这样比较友好，也便于调试。
    class Meta:
        verbose_name_plural = '文本资源'#定义对象的中文别名，用于admin显示

'''第二组'''
# 创建ResPicture对象
class ResPicture(models.Model):
    title = models.CharField(max_length=300) 
    path = models.CharField(max_length=300)   # 创建“路径”属性，长度300足够了

    def __str__(self): 
        return self.title

'''第三组'''
# 创建ResDocument对象
class ResDocument(models.Model):
    title = models.CharField(max_length=300)
    path = models.CharField(max_length=300)

    def __str__(self): 
        return self.title

'''第四组'''
# 创建ResAudio对象
class ResAudio(models.Model):
    title = models.CharField(max_length=300) 
    path = models.CharField(max_length=300)

    def __str__(self): 
        return self.title

'''第五组'''
# 创建ResVideo对象
class ResVideo(models.Model):
    title = models.CharField(max_length=300) 
    path = models.CharField(max_length=300)

    def __str__(self): 
        return self.title

'''第六组'''
# 创建ResLink对象
class ResLink(models.Model):
    title = models.CharField(max_length=300) 
    url = models.CharField(max_length=300)

    def __str__(self): 
        return self.title