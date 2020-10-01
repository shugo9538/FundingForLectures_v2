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
def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        u = request.user
        print(u.is_authenticated)
        print(u)

        if u.is_authenticated:
            user_id = request.POST['email']
            user_pw = request.POST['password']
            user = authenticate(email=user_id, password=user_pw)

            print(user)

            errorMsg = '로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요'

            if user is not None:
                request.session['name'] = user_id
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('index')
            else:
                request.session['failed'] = errorMsg
                return redirect('login')
        else:
            return  redirect('login')

    else:
        form = LoginForm()

        context = {'form': form}

        return render(request, 'users/login.html', context)


# 로그인 후 로그아웃 버튼 클릭시
class Logout(LogoutView):
    def get(self, requests):
        logout(requests)
        response = render(requests)
        response.delete_cookie('name')
        return redirect(reverse('index'))
