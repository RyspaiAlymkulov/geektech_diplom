from cart import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cart', views.CartViewSet, "cart"),
router.register(r'usercart', views.UserCartViewSet, "usercart"),
router.register(r'delivery', views.DeliveryViewSet, "delivery"),

urlpatterns = [] + router.urls
