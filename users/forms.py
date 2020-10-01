# from django.contrib.auth.models import User
from django import forms
from .models import *

# 양식 수정 필요
class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='이메일', widget=forms.EmailInput(attrs={'name': 'email'}))
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(attrs={'id': "mbpw1", 'name': 'mbpw1'}), min_length=3)
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput(attrs={'id': "mbpw_re1"}))
    CHOICES = [('student', '수강생'), ('teacher', '강사')]
    userType = forms.ChoiceField(label='사용자 유형', choices=CHOICES, widget=forms.RadioSelect(attrs={'name': 'chkbox'}), initial='수강생')
    pr = forms.CharField(label='자기소개', widget=forms.Textarea(attrs={'rows': 10, 'cols': 100, 'maxlength': 500, 'onkeyup': "counter()", 'id': "txt1", 'name': 'textarea1'}))
    career = forms.CharField(label='경력사항', widget=forms.Textarea(attrs={'rows': 10, 'cols': 100, 'maxlength': 500, 'onkeyup': "counter()", 'id': "txt2", 'name': 'textarea2'}))

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'userType', 'pr', 'career']

    def clean(self):
        cd = self.cleaned_data
        return cd
    # def clean(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Passwords not matched!')
    #     return cd['password2']

class LoginForm(forms.Form):
    email = forms.EmailField(label='이메일', widget=forms.EmailInput(attrs={'name': 'email', 'class': 'form-control'}))
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(attrs={'name': 'password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'password']