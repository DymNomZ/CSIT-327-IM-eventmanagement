from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('createStudent/', views.RegisterStudentView.as_view(), name='register_student'),
    path('createTeacher/', views.RegisterTeacherView.as_view(), name='register_teacher'),
    path('editProfile/', views.EditProfileView.as_view(), name='edit_profile'),
    path('display_available_events/', views.DisplayEventsView.as_view(), name='display_available_events'),
    path('<int:event_id>/attend/', views.AttendEventView.as_view(), name='attend_event'),
]