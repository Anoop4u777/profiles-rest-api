from django.urls import path, include

from rest_framework import routers

from profiles_api import views

router = routers.DefaultRouter()

router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
"""
In the below registerwe need not assign the base name as we
have defined it in the UserProfileViewSet using the keyword 'queryset'.
Hence rest framework will Automatically assign a base name for it.
"""
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
