from django.urls import path, include

from tasks.views import index, TaskList, TaskUpdate, TaskDelete

app_name = 'tasks'
urlpatterns = [
    path('', TaskList.as_view(), name='list'),
    path('update/<int:my_id>/', TaskUpdate.as_view(), name='update'),
    path('delete/<int:my_id>/', TaskDelete.as_view(), name='delete'),

]