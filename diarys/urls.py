from django.urls import path
from . import views

app_name = 'diarys'

urlpatterns = [
    path('', views.IndexView.as_view(), name = "index")

    ]