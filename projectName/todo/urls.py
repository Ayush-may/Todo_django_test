from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('login_user/' ,views.login_user, name='login_user'),
    path('create_user/' ,views.create_user, name='create_user'),
    path('logout_user/' ,views.logout_user, name='logout_user'),
    path('list/' ,views.list, name='list'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]