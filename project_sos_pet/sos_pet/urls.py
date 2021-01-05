
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    # path('pet/user/', views.list_user_pets),
    # path('pet/all/', views.list_all_pets),
    # path('pet/detail/<slug:id>/', views.pet_detail),
    # path('pet/register/', views.register_pet),
    # path('pet/register/submit', views.set_pet),
    # path('pet/delete/<slug:id>/', views.delete_pet),
    path('', views.index),
    
]
