from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('',ContactViewSet,basename='contact')
urlpatterns = [
   path('view/',include(router.urls)),
]
