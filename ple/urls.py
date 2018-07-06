from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('login/',views.login_page,name="login_page"),#用户登录页面
  path('user_login/',views.user_login,name="user_login"),#处理用户登录
  path('logout/', auth_views.logout, {'template_name': 'logout.html'}, name='user_logout'),#退出登录
  path('register/', views.register, name='user_register'),#用户注册
  path('course/',views.course_list,name="ple_course"),#课程列表
  path('course/<int:course_id>/',views.course_show,name="ple_course_show"),#显示课程内容
  path('course/<int:course_id>/elective/',views.elective,name="ple_elective"),#选课
  path('my_course/',views.my_course_list,name="ple_my_course"),#我的课程列表

  path('ajax_login/',views.ajax_login,name="ajax_login"),#处理ajax用户登录
]