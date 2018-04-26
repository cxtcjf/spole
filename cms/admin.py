from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Course)

class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('course','title','parent','level',)
admin.site.register(Syllabus,SyllabusAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('course','sno','name','role')
admin.site.register(Member,MemberAdmin)

class CompletionAdmin(admin.ModelAdmin):
    list_display = ('course','syllabus','member','complete','complete_at')
admin.site.register(Completion,CompletionAdmin)

class GradeAdmin(admin.ModelAdmin):
    list_display = ('course','member','item','score','grader')
admin.site.register(Grade,GradeAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('course','title','qtype','score')
admin.site.register(Question,QuestionAdmin)

class OptionAdmin(admin.ModelAdmin):
    list_display = ('question','content','correct')
admin.site.register(Option,OptionAdmin)