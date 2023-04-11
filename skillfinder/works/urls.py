from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('work/', work, name='work'),
    path('post/<int:post_id>/', show_post, name='post'),
]