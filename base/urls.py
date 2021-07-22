from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),

    path('categories/', views.get_categories, name='categories'),
    path('user/', include('base.users.urls')),
    path('courses/', include('base.courses.urls')),
]
