from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_courses, name='courses'),
    path('<pk>', views.get_course, name='course'),
    path('<pk>/content/', views.get_course_content, name='course_content'),

    # path('enroll/', views.enroll, name='enroll'),

    path('create/', views.create_course, name='course_create'),
    path('upload/', views.upload_course_image, name='course_image_upload'),
    path('update/', views.update_course, name='course_update'),
    path('delete/', views.delete_course, name='course_delete'),

]
