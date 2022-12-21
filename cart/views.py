from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from cart.models import Cart, DeliveryCost
from cart.serializers import CartSerializer, UserCartSerializer, DeliveryCostSerializer
from user.models import CustomUser


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, ]


class UserCartViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, ]
    queryset = CustomUser.objects.all()
    serializer_class = UserCartSerializer


class DeliveryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, ]
    queryset = DeliveryCost.objects.all()
    serializer_class = DeliveryCostSerializer
