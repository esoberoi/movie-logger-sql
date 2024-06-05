"""
URL configuration for sqlproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from movieapp import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('view_logs/', views.view_logs, name='view_logs'),
    path('add_log/', views.add_log, name='add_log'),
    path('delete_movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('report_form/', views.report, name='report'),
    path('update_movie_log/', views.update_movie_log, name='update_movie_log'),
]
