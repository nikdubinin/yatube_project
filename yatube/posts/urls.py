# posts/urls.py
from django.urls import path

from . import views

# Эта строчка обязательна.
# Без неё namespace работать не будет:
# namespace должен быть объявлен при include и тут, в app_name
app_name = 'posts'

urlpatterns = [
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    path('', views.index, name='index'),
]
