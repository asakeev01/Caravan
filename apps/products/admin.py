from django.contrib import admin

from .models import *


admin.site.register(Product)
admin.site.register(Colour)
admin.site.register(Size)
admin.site.register(ProductItem)
admin.site.register(Quantity)