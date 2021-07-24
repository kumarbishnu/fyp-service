from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_courses, name='courses'),
    path('<pk>', views.get_course, name='course'),
    path('<pk>/content/', views.get_course_content, name='course_content'),

    path('<pk>/enroll/', views.enroll, name='enroll'),

    path('create/', views.create_course, name='course_create'),
    path('delete/<pk>', views.delete_course, name='course_delete'),
    path('update/', views.update_course, name='course_update'),
    path('upload/', views.upload_course_image, name='course_image_upload'),

    path('chapter/create/', views.create_chapter, name='chapter_create'),
    path('chapter/delete/<pk>', views.delete_chapter, name='chapter_delete'),
    path('chapter/update/', views.update_chapter, name='chapter_update'),

    path('lecture/create/', views.create_lecture, name='lecture_create'),
    path('lecture/delete/<pk>', views.delete_lecture, name='lecture_delete'),
    path('lecture/update/', views.update_lecture, name='lecture_update'),
    path('lecture/upload/', views.upload_lecture_file, name='lecture_file_upload'),

    path('resource/create/', views.create_resource, name='resource_create'),
    path('resource/delete/<pk>', views.delete_resource, name='resource_delete'),
    path('resource/update/', views.update_resource, name='resource_update'),

]
