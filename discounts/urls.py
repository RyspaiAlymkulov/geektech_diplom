from discounts import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'discount', views.MagazineDiscountViewSet, "discount"),


urlpatterns = [] + router.urls
