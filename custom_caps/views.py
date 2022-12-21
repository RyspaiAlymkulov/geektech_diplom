from rest_framework import generics, viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from custom_caps.filters import CapsFilter
from custom_caps.models import Manufacturer, Caps, UserCapsRelation, Category
from custom_caps.serializers import ManufacturerSerializer, CapsSerializer, \
    UserCapsRelationSerializer, CategorySerializer
from rest_framework import generics, filters
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from user.permissions import IsStaffUser
from .pagination import CapsPagination


class MainMenuListAPIView(ListAPIView):
    queryset = Caps.objects.all()
    serializer_class = CapMainMenuSerializer
    permission_classes = [IsAuthenticated]


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListCreateSerializer
    permission_classes = [IsAuthenticated]


class CapsListAPIview(viewsets.ModelViewSet):
    queryset = Caps.objects.all()
    serializer_class = CapsSerializer
    pagination_class = CapsPagination
    permission_classes = [IsStaffUser]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = CapsFilter
    authentication_classes = [JWTAuthentication, ]
    search_fields = ('name', 'description', 'category', 'size', 'manufacturer', 'price')
    ordering_fields = ('price', '-price', 'rate', 'created_at',)
    name = 'caps-list'


class BrandUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandUpdateDeleteSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class CategoryUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateDeleteSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class CapsUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Caps.objects.all()
    serializer_class = CapUpdateDeleteSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class ManufacturerListAPIview(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    pagination_class = PageNumberPagination
    authentication_classes = [JWTAuthentication, ]
    name = 'manufacturer-list'


class ManufacturerItemUpdateDeleteAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, ]
    name = 'manufacturer-detail'
    lookup_field = 'id'


class UserCapsRelationAPIview(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsStaffUser]
    queryset = UserCapsRelation.objects.all()
    serializer_class = UserCapsRelationSerializer
    authentication_classes = [JWTAuthentication, ]

    def get_object(self):
        obj, _ = UserCapsRelation.objects.get_or_create(user=self.request.user,
                                                        user_id=self.kwargs['caps'])
        return obj


