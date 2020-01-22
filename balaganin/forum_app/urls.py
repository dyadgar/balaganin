from django.urls import path, include
from django.conf import settings
from . import views
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('index/', views.postlist, name='index'),
    # path('<slug:slug>/', views.post_detail, name='post_detail'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),

]