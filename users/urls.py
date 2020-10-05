from django.urls import path
from . import views

urlpatterns = [
    # 회원가입
    path('join/', views.join, name='join'), # 회원가입 버튼 클릭
    path('join/article/', views.article, name='article'), # 회원가입 버튼 클릭 후 사용 약관 확인 페이지
    path('join/enrollment/', views.enrollment, name='enrollment'), # 약관 확인후 동의 시 페이지 이동

    # 로그인 창
    path('login/', views.Login.as_view(), name='login'), # 로그인 버튼 클릭 시
    # path('googleLogin/', views.login, name='googleLogin'), # 구글 로그인

    # 로그아웃 버튼
    path('logout/', views.Logout.as_view(), name='logout'),
]
