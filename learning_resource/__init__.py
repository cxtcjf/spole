from django.apps import AppConfig
import os
#admin里的app名称显示为中文名
default_app_config = 'learning_resource.Learning_resourceConfig'
VERBOSE_APP_NAME = u"课程资源"
 
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]
 
class Learning_resourceConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME