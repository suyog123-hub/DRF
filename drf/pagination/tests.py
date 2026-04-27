from django.test import TestCase
from rest_framework.test import APIRequestFactory,force_authenticate
from .views import DetailsViewSet
# Create your tests here.
# unit testing --> testing the smallest part of the code 
# interation testing --> testing one or more than one component at a time (api client ,Api test case )

#API Request factory  --> low- level testing bypass http throtlling 



factory = APIRequestFactory()

request = factory.get("/pagination/details")
view = DetailsViewSet.as_view({'get':"list","post":"list"})
response = view(request)

print(response.status_code)