from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet
from logistic.views import StockViewSet


router = DefaultRouter()
router.register(prefix='products', viewset=ProductViewSet)
router.register(prefix='stocks', viewset=StockViewSet)

urlpatterns = router.urls
