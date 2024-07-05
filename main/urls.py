from . import views
from .views import *
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.home, name="homePage"),
    path('product/detail/<int:pk>', productDetail.as_view(),name='detail')
]
