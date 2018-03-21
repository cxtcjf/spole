from django.urls import path
from . import views

urlpatterns = [
  path('article_list',views.res_article_list),
]