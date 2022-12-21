from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from discounts.models import MagazineDiscount
from discounts.serializers import MagazineDiscountSerializer
from user.permissions import IsStaffUser


class MagazineDiscountViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaffUser]
    authentication_classes = [JWTAuthentication, ]
    queryset = MagazineDiscount.objects.all()
    serializer_class = MagazineDiscountSerializer

