from django.contrib import admin
from .models import *
# Register your models here.

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('code','title','begin','end',)
admin.site.register(Assignment,AssignmentAdmin)

class SolutionAdmin(admin.ModelAdmin):
    list_display = ('assignment','sno','name','created',)
admin.site.register(Solution,SolutionAdmin)