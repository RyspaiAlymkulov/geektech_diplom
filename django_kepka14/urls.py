from django.contrib import admin
from django.urls import path, include
from .swagger import urlpatterns as swagger_urls
from custom_caps import views
from rest_framework import routers
from cart.urls import urlpatterns as cart_urls
from discounts.urls import urlpatterns as discount_urls

router = routers.DefaultRouter()
router.register(r'caps', views.CapsListAPIview)
router.register(r'userrelation', views.UserCapsRelationAPIview, basename='userrelation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/v1/', include(router.urls)),
    path(r'api/v1/', include(router.urls)),


    path('api/v1/user/', include('user.urls')),
    path('api/v1/socialMedia/', include('social_media.urls')),

    path(r'api/v1/', include(router.urls)),
    path('caps/<int:id>/', views.CapsUpdateDeleteAPIView.as_view()),
    path('api/v1/maimmenu/', views.MainMenuListAPIView.as_view()),
    path('categories/', views.CategoryListCreateAPIView.as_view()),
    path('brands/<int:id>/', views.BrandUpdateDeleteAPIView.as_view()),
    path('categories/<int:id>/', views.CategoryUpdateDeleteAPIView.as_view()),
    path('manufacturer/', views.ManufacturerListAPIview.as_view()),
    path('manufacturer/<int:id>/', views.ManufacturerItemUpdateDeleteAPIview.as_view()),

    ] + cart_urls + swagger_urls + discount_urls


