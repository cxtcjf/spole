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