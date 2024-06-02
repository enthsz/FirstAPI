from django.urls import path
from . import views

urlpatterns = [
    path('', views.listTask),
    path('list-detail/<int:pk>/', views.list_detail),
    path('create-task', views.create_task),
    path('list-update/<int:pk>/', views.list_update),
    path('task-delete/<int:pk>/', views.delete_task)
]
