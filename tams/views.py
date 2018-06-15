from django.shortcuts import render
from .models import *
# Create your views here.
#列出所有作业
def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, "assignment_list.html",{"assignments":assignments})

#根据id，查询作业
def assignment_show(request,assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    return render(request, "assignment_content.html",{"assignment":assignment})

#根据作业id，查询作业完成情况
def solution_list(request,assignment_id):
    solutions = Solution.objects.filter(assignment_id=assignment_id)
    return render(request, "solution_list.html",{"solutions":solutions})

#根据id，查询学生上交作业详情
def solution_show(request,solution_id):
    solution = Solution.objects.get(id=solution_id)
    return render(request, "solution_content.html",{"solution":solution})

#列出所有测验
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, "exam_list.html",{"exams":exams})

#根据id，查询测验详情
def exam_show(request,exam_id):
    exam = Exam.objects.get(id=exam_id)
    return render(request, "exam_content.html",{"exam":exam})

#根据测验id，查询试卷所有试题
def exampaper_show(request,exam_id):
    exampaper = ExamPaper.objects.filter(exam_id=exam_id)
    return render(request, "exampaper_content.html",{"exampaper":exampaper})

#根据测验id，查询所有答卷
def answerpaper_show(request,exam_id):
    answers = AnswerPaper.objects.filter(exam_id=exam_id)
    return render(request, "answer_list.html",{"answers":answers})