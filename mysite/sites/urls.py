
from django.urls import path,include
from rest_framework import routers
from .views import *


router = routers.SimpleRouter()

router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'property', PropertyViewSet, basename='property')
router.register(r'booking', BookingViewSet, basename='booking')
router.register(r'review', ReviewViewSet, basename='review')
router.register(r'photos', PhotosViewSet, basename='photos')


urlpatterns = [
    path('',include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]