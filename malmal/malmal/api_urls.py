from django.conf.urls import include
from django.conf.urls import url


urlpatterns = [
    url('', include('diet.urls')),
    url('', include('shopping.urls')),
]
