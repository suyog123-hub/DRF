from rest_framework import viewsets
from .models import Details
from .serailizaer import DetailsSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .custompagination import DetailsPagination
from .customthrottling import CustomUserRateThrottle
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class DetailsViewSet(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer
    permission_classes = [AllowAny]
    # pagination_class = DetailsPagination
    throttle_classes = [CustomUserRateThrottle]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'age']
    search_fields = ['name']
    ordering_fields = ['name', 'age']



# custom filtering without using django filter backend

    # def get_queryset(self):
    #     queryset = Details.objects.all()
    #     name = self.request.query_params.get('name')
    #     age = self.request.query_params.get('age')

    #     if name is not None:
    #         queryset = queryset.filter(name__icontains=name)
    #     else:
    #         queryset = Details.objects.all()

    #     if age is not None: 
    #         queryset = queryset.filter(age__gt=age)
    #     else:
    #         queryset = Details.objects.all()
        
    #     return queryset
    