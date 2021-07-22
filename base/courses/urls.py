from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_courses, name='courses'),
    path('<pk>', views.get_course, name='course'),
    path('<pk>/content/', views.get_course_content, name='course_content'),
]
