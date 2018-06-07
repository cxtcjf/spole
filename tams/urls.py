from django.urls import path
from . import views

urlpatterns = [
     path('assignment',views.assignment_list,name="assignment"),#作业列表
     path('assignment/<int:assignment_id>/',views.assignment_show,name="assignment_show"),#显示作业内容
     path('assignment/<int:assignment_id>/solution',views.solution_list,name="solution"),#显示本次作业的上交情况
     path('solution/<int:solution_id>/',views.solution_show,name="solution_show"),#显示作业详情
]