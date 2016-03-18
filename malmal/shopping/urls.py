from rest_framework.routers import SimpleRouter

from shopping.views import ShoppingListViewSet


router = SimpleRouter()
router.register('shopping', ShoppingListViewSet)

urlpatterns = router.urls
