from django.urls import path,include
from .views import DetailsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('details',DetailsViewSet,basename='details')

urlpatterns = [
    path('',include(router.urls))
]
