
from django.contrib import admin
from django.urls import path, include
from works.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('works.urls')),
]
