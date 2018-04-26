from django.urls import path
from . import views

urlpatterns = [
  path('course',views.course_list,name="course"),
  path('course/<int:course_id>/',views.course_show,name="course_show"),
  path('course/<int:course_id>/syllabus',views.syllabus_list,name="syllabus"),
]