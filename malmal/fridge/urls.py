from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from fridge.views import FridgeViewSet


router = SimpleRouter()
router.register('fridge', FridgeViewSet)

urlpatterns = []
#     url(r'diet/(?P<pk>\d+)/createlist/?', GenerateShoppingListView.as_view()),
# ]

urlpatterns.extend(router.urls)
