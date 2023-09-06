from django.contrib import admin
# Register your models here.
from .models import NeredenNereye, Cars, Ekstra, YolcuLast, YolcuBilgi

admin.site.register(NeredenNereye)
admin.site.register(Cars)
admin.site.register(Ekstra)
admin.site.register(YolcuLast)
admin.site.register(YolcuBilgi)