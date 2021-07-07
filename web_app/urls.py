from django.urls import path

from . import views

app_name = 'web_app'

urlpatterns = [
    path('', views.MyBaseView.as_view(), name='index'),
]