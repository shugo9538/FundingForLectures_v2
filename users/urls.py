from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
import config.urls

urlpatterns = [
    # 회원가입
    path('join/', views.join, name='join'), # 회원가입 버튼 클릭
    path('join/enrollment/', views.enrollment, name='enrollment'), # 약관 확인후 동의 시 페이지 이동
    path('join/enrollment/create', views.create, name='create'), # 가입 정보 기입 후 계정 생성

    # 로그인 창
    path('login/', views.Login.as_view(), name='login'), # 로그인 버튼 클릭 시
    path('googleLogin/', views.Login.as_view(), name='googleLogin'), # 구글 로그인

    # 로그아웃 버튼
    path('logout/', views.Logout.as_view(), name='logout'),
]
