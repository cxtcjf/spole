from django.shortcuts import render
from .models import Course,Syllabus

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, "course_list.html",{"courses":courses})

#根据id，查询课程对象
def course_show(request,course_id):
    course = Course.objects.get(id=course_id)
    return render(request, "course_content.html",{"course":course,"course_id":course_id})

#根据id，查询课程的所有大纲节点
def display(syllabuses):
    display_list= []
    for syllabus in syllabuses:
        display_list.append(syllabus.title)
        children = syllabus.children.all()
        if len(children) > 0:
            display_list.append(display(children))
    return display_list

def syllabus_list(request,course_id):
    syllabus_roots = Syllabus.objects.filter(parent=None)
    return render(request, "syllabus_list.html",{"syllabuses":display(syllabus_roots),"course_id":course_id})