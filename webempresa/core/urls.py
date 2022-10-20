
from django.urls import path
from . import views 

urlpatterns = [
    # Paths del core
    path('', views.home,name="home"),
    path('home/', views.home,name="home_2"),
    path('about/', views.about,name="about"),
    path('store/', views.store,name="store"),
]
