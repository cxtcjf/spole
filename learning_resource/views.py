from django.shortcuts import render
from .models import ResArticle #第1组
#第2组 from .models import Picture
#第3组 from .models import Document
#第4组 from .models import Audio
#第5组 from .models import Video
#第6组 from .models import Link 

# Create your views here.
# 第1组
# 视图函数，用于响应用户请求，读取文章列表
def res_article_list(request):
    #通过ResArticle对象，从数据库中读取所有的文章
    articles = ResArticle.objects.all()
    #将数据articles渲染到模板文件article_list.html，生成网页返回给用户
    return render(request, "res_article_list.html",{"articles":articles})

'''第2组到第6组的代码，依此类推'''