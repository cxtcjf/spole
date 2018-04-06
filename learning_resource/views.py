from django.shortcuts import render
from .models import ResArticle #第1组
from .models import ResPicture
#第3组 from .models import ResDocument
#第4组 from .models import ResAudio
#第5组 from .models import ResVideo
from .models import ResLink #第6组

import urllib.request

# Create your views here.
# 第1组
# 视图函数，用于响应用户请求，读取文章列表
def res_article_list(request):
    #通过ResArticle对象，从数据库中读取所有的文章
    articles = ResArticle.objects.all()
    #将数据articles渲染到模板文件article_list.html，生成网页返回给用户
    return render(request, "res_article_list.html",{"articles":articles})

#根据id，查询特定文章对象
def res_article_show(request,res_article_id):
    article = ResArticle.objects.get(id=res_article_id)
    return render(request, "res_article_content.html",{"article":article})


def res_picture_list(request):
    pictures = ResPicture.objects.all()
    return render(request, "res_picture_list.html",{"pictures":pictures})
    
def res_picture_show(request,res_picture_id):
    picture = ResPicture.objects.get(id=res_picture_id)
    return render(request, "res_picture_content.html",{"picture":picture})

def res_link_list(request):
    links = ResLink.objects.all()
    return render(request, "res_link_list.html",{"links":links})
    
def res_link_show(request,res_link_id):
    link = ResLink.objects.get(id=res_link_id)
    try:
        res = urllib.request.urlopen(link.url)#打开链接 
        code = res.getcode()#返回http连接代码，正常会返回代码200
        res.close()#关闭网络连接
    except:#如果打开链接出错会被捕获
        code = 44#返回错误代码
    return render(request, "res_link_content.html",{"link":link,"code":code})