from rest_framework.routers import SimpleRouter

from diet.views import DietViewSet


router = SimpleRouter()
router.register('diet', DietViewSet)

urlpatterns = router.urls
