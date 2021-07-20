from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),

    path('categories/', views.get_categories, name='categories'),

    path('courses/', views.get_courses, name='courses'),
    path('courses/<pk>', views.get_course, name='course'),

    path('user/profile/', views.get_user_profile, name='user_profile'),
    path('user/login/', views.MyTokenObtainPairView.as_view(), name='login'),
]
