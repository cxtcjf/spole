"""spole URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings##
from django.conf.urls.static import static##

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resource/', include('learning_resource.urls')), #添加应用自己的url定义文件
    path('ckeditor/', include('ckeditor_uploader.urls')),#添加ckeditor支持
    path('cms/', include('cms.urls')),#添加cms自己的url定义文件
    path('tams/', include('tams.urls')),#添加tams自己的url定义文件
    path('ple/', include('ple.urls')),#添加ple的url定义文件
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)##