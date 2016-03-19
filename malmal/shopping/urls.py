from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from shopping.views import CompareFridgeListView
from shopping.views import ShoppingListViewSet


router = SimpleRouter()

urlpatterns = [
    url(r'shopping/(?P<pk>\d+)/comparefridge/?', CompareFridgeListView.as_view()),
]

router.register('shopping', ShoppingListViewSet)

urlpatterns.extend(router.urls)
