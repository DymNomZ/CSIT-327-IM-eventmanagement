from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('account/', views.LoginPageView.as_view(), name='login'),
]