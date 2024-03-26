from django.urls import path
from .views import add_task, delete_task, update_task, list_tasks

urlpatterns = [
    path('add/', add_task, name='add_task'),
    path('delete/', delete_task, name='delete_task'),
    path('update/', update_task, name='update_task'),
    path('list/', list_tasks, name='list_tasks'),
]
