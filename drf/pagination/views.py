from rest_framework import viewsets
from .models import Details
from .serailizaer import DetailsSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .custompagination import DetailsPagination
from .customthrottling import CustomUserRateThrottle
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
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

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self,request, *args , **kwargs):
        return super().list(request, *args, **kwargs)




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
    