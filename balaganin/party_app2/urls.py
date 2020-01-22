from django.urls import path, include
from party_app2 import views

urlpatterns = [
    path('create/', views.index2, name='index2'),
    path('filter/', views.EventListView.as_view(), name='list'),
]