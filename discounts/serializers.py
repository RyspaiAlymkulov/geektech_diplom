from discounts.models import MagazineDiscount
from rest_framework import serializers


class MagazineDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineDiscount
        fields = '__all__'



