from django.shortcuts import render, redirect
from django.urls import reverse

from users.models import *

# Create your views here.
def edit(request):
    return render(request, 'mypage/correction.html')

def edit_info(request):
    user_id = request.session['name']
    presenet_pw = request.POST.get('mbpw_present')
    edit_pw = request.POST.get('mbpw')
    edit_pwchk = request.POST.get('mbpw_re1')

    errorMsg = '변경할 비밀번호를 다시 확인해주세요'

    if User.objects.filter(email=user_id) and User.objects.filter(password=presenet_pw):
        if edit_pw == edit_pwchk:
            updateUser = User.objects.get(email=user_id)
            updateUser.password = edit_pw
            updateUser.save()
            request.session['failed'] = None
        else:
            request.session['failed'] = errorMsg
    return redirect(reverse('edit'))

def withdrawal(request):
    return render(request, 'mypage/withdrawal.html')

def doWithdrawal(request):
    try:
        user_id = request.session['name']
        user = User.objects.get(email=user_id)
        user.delete()
        request.session['name'] = None
    except:
        request.session['msg'] = "error"
    return render(request, 'mainpage/index.html')

def lecturefunding(request):
    return render(request, 'mypage/lecturefunding.html')

def student(request):
    return render(request, 'mypage/student.html')

def teacher(request):
    return render(request, 'mypage/teacher.html')