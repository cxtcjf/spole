from django.urls import path
from . import views

urlpatterns = [
  path('course',views.course_list,name="course"),
  path('course/<int:course_id>/',views.course_show,name="course_show"),
  path('course/<int:course_id>/syllabus',views.syllabus_list,name="syllabus"),
  path('course/<int:course_id>/syllabus/<int:syllabus_id>/',views.syllabus_show,name="syllabus_show"),
  path('course/<int:course_id>/members',views.member_list,name="members"),
  path('course/<int:course_id>/completions',views.completion_list,name="completions"),
  path('course/<int:course_id>/completions/<int:member_id>/',views.completion_show,name="completion_show"),
  path('course/<int:course_id>/grades',views.grade_list,name="grades"),
  path('course/<int:course_id>/grades/<int:member_id>/',views.grade_show,name="grade_show"),
  path('course/<int:course_id>/questions',views.question_list,name="questions"),
]