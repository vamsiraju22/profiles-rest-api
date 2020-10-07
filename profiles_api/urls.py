from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, base_name= 'hello-viewset')

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()), #When we load the project. It will first checking with
    path('',include(router.urls))
]
