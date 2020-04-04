from django.contrib import admin 
from django.urls import path,include
from .view import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('', homepage),
    path('articles/', include('articles.urls'))
]
