from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.listTask, name='list-tasks'),
    path('list-detail/<int:pk>/', views.list_detail, name='list-detail'),
    path('create-task', views.create_task, name='create-task'),
    path('list-update/<int:pk>/', views.list_update, name='list-update'),
    path('task-delete/<int:pk>/', views.delete_task, name='delete-task'),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain-token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh-token')
]
