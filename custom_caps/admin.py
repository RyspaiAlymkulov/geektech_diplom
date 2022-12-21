from django.contrib import admin
from custom_caps.models import Manufacturer, Caps, UserCapsRelation, Category, Brand, Collection, Size

admin.site.register(Brand),
admin.site.register(Manufacturer)
admin.site.register(Caps)
admin.site.register(UserCapsRelation)
admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Size)

