from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse

from .models import *

# 회원가입
def join(request):
    request.session['failed'] = None
    return render(request, 'users/article.html')

def enrollment(request):
    return render(request, 'users/enrollment.html')

def create(request):
    createEmail = request.POST['email']
    createPassword = request.POST['mbpw1']

    if request.POST['chkbox'] == True :
        createUserType = True
        createPr = None
        createCareer = None
    else:
        createUserType = False
        createPr = request.POST.get('textarea1')
        createCareer = request.POST.get('textarea2')

    createUser = User(email=createEmail,
                      password=createPassword,
                      userType=createUserType,
                      pr=createPr,
                      career=createCareer)

    if User.objects.filter(email=createEmail):
        request.session['failed'] = "이미 존재하는 이메일입니다."
        return redirect(reverse('enrollment'))
    else:
        request.session['failed'] = None
        createUser.save()

    return redirect(reverse('index'))

# 구글 계정 연동 추가 중
def auth_allowed(backend, uid, user=None, *args, **kwargs):
    print("backend >>", backend)
    print("uid >>", uid)
    print("user >>", user)
    print("args >>", args)
    print("kwargs >>", kwargs)

    return redirect(reverse('index'))

# 로그인 버튼 누르는 경우 동작
class Login(LoginView):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        # 로그인 버튼 클릭시 폼(아이디, 패스워드)에서 데이터를 읽어옴
        user_id = request.POST['id']
        user_pw = request.POST['password']

        errorMsg = '로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요'

        request.session['failed'] = None

        # 읽어온 사용자 정보와 일치하는지 확인
        if User.objects.filter(email=user_id) and User.objects.filter(password=user_pw):
            request.session['name'] = user_id
        else:
            request.session['failed'] = errorMsg
            return redirect(reverse('login'))

        return redirect(reverse('index'))

# 로그인 후 로그아웃 버튼 클릭시
class Logout(LogoutView):
    def get(self, requests):
        response = render(requests)
        response.delete_cookie('name')
        return redirect(reverse('index'))



