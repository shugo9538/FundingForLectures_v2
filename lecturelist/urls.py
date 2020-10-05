from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all, name='list_all'),
    path('opening/', views.opening, name='list_opening'),
    path('funding/', views.funding, name='list_funding'),
    path('detail/<int:list_id>', views.detail, name='detail'),
]
