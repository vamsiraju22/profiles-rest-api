from django.urls import path

from profiles_api import views

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()) #When we load the project. It will first checking with
]
