from django import forms
from django.contrib.auth.models import User
from cms.models import Member

#登录表单
class LoginForm(forms.Form):
    username = forms.CharField(label="用户名",  widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="密码",  widget=forms.PasswordInput(attrs={'class':'form-control'}))

#注册表单
class RegistrationForm(forms.ModelForm):#写入数据库使用ModelForm
    username = forms.CharField(label="用户名",  widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="电子邮件",  widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="再次输入密码", widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User #要操作的数据表
        fields = ("username", "email")

    def clean_password2(self):#检验两次输入的密码是否相同
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("两次输入的密码不同")
        return cd['password2']

#选课表单
class ElectiveForm(forms.ModelForm):
    course_id = forms.IntegerField(label="课程编号",widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))#只读，用于传递数据
    name = forms.CharField(label="姓名",  widget=forms.TextInput(attrs={'class':'form-control'}))
    sno = forms.CharField(label="学号",  widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Member #要操作的数据表
        #fields = ("course","user","name", "sno","role")
        fields = ("course_id","name", "sno")

    def clean_sno(self):#检验学号是否已选过课
        cd = self.cleaned_data
        if Member.objects.filter(course_id=cd['course_id']).filter(sno=cd['sno']):
            raise forms.ValidationError("学号已选过本课程")
        return cd['sno']