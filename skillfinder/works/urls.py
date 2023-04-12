from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('findwork/', work, name='findwork'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('work/', show_work, name='work'),
    path('customer/', show_cust, name='customer'),
    path('about/', about, name='about'),
]