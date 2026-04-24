from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('contacts', Contacacountt, basename='contact')
router.register('register', userRegisterview, basename='register')
urlpatterns = [
    path('', include(router.urls)),
]