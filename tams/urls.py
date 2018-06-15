from django.urls import path
from . import views

urlpatterns = [
     path('assignment',views.assignment_list,name="assignment"),#作业列表
     path('assignment/<int:assignment_id>/',views.assignment_show,name="assignment_show"),#显示作业内容
     path('assignment/<int:assignment_id>/solution',views.solution_list,name="solution"),#显示本次作业的上交情况
     path('solution/<int:solution_id>/',views.solution_show,name="solution_show"),#显示作业详情

     path('exam',views.exam_list,name="exam"),#测验列表
     path('exam/<int:exam_id>/',views.exam_show,name="exam_show"),#显示测验内容
     path('exam/<int:exam_id>/exampaper',views.exampaper_show,name="exam_paper"),#显示本次测验的试卷
     path('exam/<int:exam_id>/answerpaper',views.answerpaper_show,name="answer_paper"),#显示本次测验的试卷
]