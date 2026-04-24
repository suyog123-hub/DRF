from django.urls import path
from .views import Genericview
urlpatterns = [
    path("",Genericview.as_view(),name='genericview'),
     
]
