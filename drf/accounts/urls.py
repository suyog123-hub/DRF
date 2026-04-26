from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('contacts', Contacacountt, basename='contact')
router.register('register', userRegisterview, basename='register')
router.register('login', loginview, basename='login')
urlpatterns = [
    path('', include(router.urls)),
]