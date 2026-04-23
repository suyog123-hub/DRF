from django.urls import path
from .views import *
urlpatterns = [
    path('test/', APITestView.as_view(), name='api-test'),
    path('test/<int:id>/', APITestView.as_view(), name='api-test-id'),
]