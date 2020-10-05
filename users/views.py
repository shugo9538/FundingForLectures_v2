from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import RegisterForm, LoginForm

# 회원가입
def join(request):
    return render(request, 'users/article.html')

def article(request):
    return render(request, 'users/article.html')

@csrf_exempt
def enrollment(request):
    if request.method == "POST":
        u = User()
        form = RegisterForm(data=request.POST, instance=u)

        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    else:
        form = RegisterForm()

    context = {'form': form}

    return render(request, 'users/enrollment.html', context)

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

        if User.objects.filter(email=user_id) and User.objects.filter(password=user_pw):
            request.session['name'] = user_id
        else:
            request.session['failed'] = errorMsg
            return redirect(reverse('login'))

        return redirect(reverse('index'))


# 로그인 후 로그아웃 버튼 클릭시
class Logout(LogoutView):
    def get(self, requests):
        logout(requests)
        response = render(requests)
        response.delete_cookie('name')
        return redirect(reverse('index'))
