from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from basic_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('admin/', admin.site.urls),
    url(r'^basic_app', include('basic_app.urls')),
    url(r'^logout/',views.user_logout,name='logout'),
    url(r'^special/',views.special,name='special'),
]
