from django.conf import settings
from . import views
from django.views.static import serve
from django.conf.urls import url
from django.urls import path, include
from profile_app import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('<username>/', views.profile, name='profile')
]
