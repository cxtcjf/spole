from django.urls import path
from . import views

urlpatterns = [
  path('article_list',views.res_article_list),
  path('article/<int:res_article_id>/',views.res_article_show),

  path('picture_list',views.res_picture_list),
  path('picture/<int:res_picture_id>/',views.res_picture_show),

  path('link_list',views.res_link_list),
  path('link/<int:res_link_id>/',views.res_link_show),
]