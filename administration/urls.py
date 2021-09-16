from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home_page, name='home_page'),
    path('login', views.admin_login, name='login'),
    path('logout', views.admin_logout, name='logout'),
    path('designation', views.add_designation, name='designation'),
    path('register', views.register, name='register'),
]
