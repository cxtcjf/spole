from django.shortcuts import render
from .models import Course,Syllabus,Member,Completion,Grade,Question,Question

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, "course_list.html",{"courses":courses})

#根据id，查询课程对象
def course_show(request,course_id):
    course = Course.objects.get(id=course_id)
    return render(request, "course_content.html",{"course":course,"course_id":course_id})

#列出教学大纲的章
def syllabus_list(request,course_id):
    syllabus_roots = Syllabus.objects.filter(course_id=course_id).filter(parent=None)
    return render(request, "syllabus_list.html",{"syllabus_roots":syllabus_roots,"course_id":course_id})

#显示教学大纲的单元内容
def syllabus_show(request,course_id,syllabus_id):
    unit = Syllabus.objects.get(id=syllabus_id)
    return render(request, "syllabus_content.html",{"unit":unit,"course_id":course_id})

#列出所有学生成员用于进度显示
def completion_list(request,course_id):
    members = Member.objects.filter(course_id=course_id).filter(role='student')
    return render(request, "completion_list.html",{"members":members,"course_id":course_id})

#列出所有成员
def member_list(request,course_id):
    members = Member.objects.filter(course_id=course_id)
    return render(request, "member_list.html",{"members":members,"course_id":course_id})

#列出所有学生成员,用于成绩显示
def grade_list(request,course_id):
    members = Member.objects.filter(course_id=course_id).filter(role='student')
    return render(request, "grade_list.html",{"members":members,"course_id":course_id})

#根据课程id和成员id，查询该成员的课程成绩
def grade_show(request,course_id,member_id):
    grades = Grade.objects.filter(course_id=course_id).filter(member_id=member_id)
    return render(request, "grade_content.html",{"grades":grades,"course_id":course_id})

#根据课程id和成员id，查询该成员的课程学习进度
def completion_show(request,course_id,member_id):
    completions = Completion.objects.filter(course_id=course_id).filter(member_id=member_id)
    return render(request, "completion_content.html",{"completions":completions,"course_id":course_id})

#列出本课程的所有题目
def question_list(request,course_id):
    questions = Question.objects.filter(course_id=course_id)
    return render(request, "question_list.html",{"questions":questions,"course_id":course_id})