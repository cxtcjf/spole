from django.shortcuts import render
from django.contrib.auth import authenticate, login#从django的内置用户认证app中引入两个方法
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from cms.models import Course
from django.contrib.auth.decorators import login_required#装饰器


# Create your views here.
def login_page(request):
    login_form = LoginForm()
    return render(request, "login.html", {"form": login_form})

#用户登录
def user_login(request):
    if request.method == "POST":#提交数据
        login_form = LoginForm(request.POST)
        if login_form.is_valid():#验证传入的数据是否合法
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                #return HttpResponse("欢迎. 登录成功！")
                return HttpResponseRedirect(reverse('ple_course'))
            else:
                return HttpResponse("对不起，您的用户名或密码错误！")
        else:
            return HttpResponse("数据无效") 

#用户注册
def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)#生成数据对象但不写入数据库
            new_user.set_password(user_form.cleaned_data['password'])#设置经过校验的密码
            new_user.save()#写入数据库
            #return HttpResponse("注册成功")
            result = 1#成功标志
        else:
            #return HttpResponse("对不起, 注册失败.")
            result = 0#失败标志
        return render(request, "register_complete.html", {"result": result})
    else:
        user_form = RegistrationForm()
        return render(request, "register.html", {"form": user_form})

@login_required(login_url='login_page')
#列出所有课程
def course_list(request):
    courses = Course.objects.all()
    return render(request, "ple_course_list.html",{"courses":courses})

#根据id，查询课程对象
def course_show(request,course_id):
    course = Course.objects.get(id=course_id)
    return render(request, "ple_course_content.html",{"course":course})

#选课
def elective(request,course_id):
    if request.method == "POST":
        elective_form = ElectiveForm(request.POST)
        if elective_form.is_valid():
            new_elective = elective_form.save(commit=False)#生成数据对象但不写入数据库
            new_elective.course_id = course_id
            new_elective.user = request.user
            new_elective.role = 'student'
            new_elective.save()#写入数据库
            #return HttpResponse("选课成功")
            result = 1
        else:
            #return HttpResponse("对不起, 选课失败.")
            result = 0
        return render(request, "ple_elective_complete.html", {"result":result,"course_id":course_id})     
    else:
        elective_form = ElectiveForm()
        elective_form.initial['course_id'] = course_id
        return render(request, "ple_elective.html", {"form": elective_form})

#我的课程
def my_course_list(request):
    members = request.user.members.all()#获取登录用户，反向查询课程成员
    return render(request, "ple_my_course_list.html",{"members":members})

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse#支持Ajax
#ajax用户登录
@csrf_exempt#暂时关闭csrf
def ajax_login(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user:
        login(request, user)
        code = 1
    else:
        code = 0
    return JsonResponse(code,safe=False)