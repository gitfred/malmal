from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from diet.views import DietViewSet
from diet.views import GenerateShoppingListView


router = SimpleRouter()
router.register('diet', DietViewSet)

urlpatterns = [
    url(r'diet/(?P<pk>\d+)/createlist/?', GenerateShoppingListView.as_view()),
]

urlpatterns.extend(router.urls)
