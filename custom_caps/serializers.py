from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError


class CapMainMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caps
        fields = 'id name categories sizes description image manufacturer currency price created_at collection brand'.split()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name caps'.split()


class CategoryValidateAbstractSerializer(CategorySerializer, serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=100)
    caps = CapMainMenuSerializer(many=True, required=False)

    def validate_id(self, id):
        try:
            Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise ValidationError('not found')
        return id


class CategoryListCreateSerializer(CategoryValidateAbstractSerializer):
    def validate_name(self, name):
        try:
            Category.objects.get(name=name)
        except Category.DoesNotExist:
            return name
        raise ValidationError('name is already taken')


class CategoryUpdateDeleteSerializer(CategoryValidateAbstractSerializer):
    def validate_name(self, name):
        try:
            Category.objects.exclude(id=self.context.get('id')).get(name=name)
        except Category.DoesNotExist:
            return name
        raise ValidationError('name is already taken')


class CapsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=3, max_length=100, required=False, write_only=True)
    likes_count = serializers.SerializerMethodField()
    manufacturer = serializers.SlugRelatedField(
        queryset=Manufacturer.objects.all(), slug_field='name')
    currency = serializers.ChoiceField(
        choices=Caps.CURRENCY_CHOICES)
    currency_name = serializers.CharField(
        source='get_currency_display',
        read_only=True)

    class Meta:
        model = Caps
        fields = '__all__'

    def get_likes_count(self, instance):
        return UserCapsRelation.objects.filter(caps=instance, like=True).count()

    def validate_id(self, id):
        try:
            Caps.objects.get(id=id)
        except Caps.DoesNotExist:
            raise ValidationError('not found')
        return id


class CapListCreateSerializer(CapsSerializer):
    def validate_name(self):
        if self.name:
            try:
                Caps.objects.get(name=self.name)
            except Caps.DoesNotExist:
                return self.name
            raise ValidationError('name is already taken')
        return


class CapUpdateDeleteSerializer(CapsSerializer):
    def validate_name(self):
        if self.name:
            try:
                Caps.objects.exclude(id=self.context.get('id')).get(name=self.name)
            except Caps.DoesNotExist:
                return self.name
            raise ValidationError('name is already taken')
        return


class BrandSerializer(serializers.ModelSerializer):
    caps = CapMainMenuSerializer(many=True, required=False)

    class Meta:
        model = Brand
        fields = 'id name caps'.split()


class BrandValidateAbstractSerializer(BrandSerializer, serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=100)
    image = serializers.ImageField()

    def validate_id(self, id):
        try:
            Brand.objects.get(id=id)
        except Brand.DoesNotExist:
            raise ValidationError('not found')
        return id


class BrandListCreateSerializer(BrandValidateAbstractSerializer):
    def validate_name(self, name):
        try:
            Brand.objects.get(name=name)
        except Brand.DoesNotExist:
            return name
        raise ValidationError('name is already taken')


class BrandUpdateDeleteSerializer(BrandValidateAbstractSerializer):
    def validate_name(self, name):
        try:
            Brand.objects.exclude(id=self.context.get('id')).get(name=name)
        except Brand.DoesNotExist:
            return name
        raise ValidationError('name is already taken')


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = '__all__'


class UserCapsRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCapsRelation
        fields = '__all__'
