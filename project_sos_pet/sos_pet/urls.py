
from django.contrib import admin
from django.urls import path, include
from core import views
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showcase),
    path('detail/<slug:id>/', views.showdetail),   
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('pet/user/', views.list_user_pets),
    path('pet/all/', views.list_all_pets),
    path('pet/dog/', views.list_dog_pets),
    path('pet/cat/', views.list_cat_pets),
    path('pet/detail/<slug:id>/', views.pet_detail),
    path('pet/register/', views.register_pet),
    path('pet/register/submit', views.set_pet),
    path('pet/delete/<slug:id>/', views.delete_pet),

    path('accounts/', include('allauth.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)