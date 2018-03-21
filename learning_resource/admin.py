from django.contrib import admin
'''各组引入自己的对象'''
from .models import ResArticle #第1组
#第2组 from .models import ResPicture
#第3组 from .models import ResDocument
#第4组 from .models import ResAudio
#第5组 from .models import ResVideo
#第6组 from .models import ResLink
# Register your models here.
admin.site.site_header = '楚雄师范学院SPOLE课程管理系统' # 此处设置页面显示标题
admin.site.site_title = '楚雄师院SPOLE' # 此处设置页面头部标题
admin.site.register(ResArticle) #第1组
#第2组-第6组以此类推