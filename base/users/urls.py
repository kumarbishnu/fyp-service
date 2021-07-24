from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('register/', views.register_user, name='register'),

    path('profile/', views.get_user_profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/upload/', views.upload_user_image, name='update_profile'),

    path('courses/', views.get_user_courses, name='user_courses'),
]
