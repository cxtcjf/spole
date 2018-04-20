from django.urls import path
from . import views

urlpatterns = [
  path('article',views.res_article_list),
  path('article/<int:res_article_id>/',views.res_article_show),

  path('picture',views.res_picture_list),
  path('picture/<int:res_picture_id>/',views.res_picture_show),

  path('document',views.res_document_list),
  path('document/<int:res_document_id>/',views.res_document_show),

  path('audio',views.res_audio_list),
  path('audio/<int:res_audio_id>/',views.res_audio_show),

  path('video',views.res_video_list),
  path('video/<int:res_video_id>/',views.res_video_show),

  path('link',views.res_link_list),
  path('link/<int:res_link_id>/',views.res_link_show),
]