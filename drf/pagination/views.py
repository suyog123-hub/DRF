from rest_framework import viewsets
from .models import Details
from .serailizaer import DetailsSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .custompagination import DetailsPagination
from .customthrottling import CustomUserRateThrottle



class DetailsViewSet(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer
    permission_classes = [AllowAny]
    pagination_class = DetailsPagination
    throttle_classes = [CustomUserRateThrottle]