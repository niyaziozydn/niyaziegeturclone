from django.urls import path, include
# lookup field vermezsek auto pk olarak geliyo 
from .views import CarCreate,  YolcularAllview, YolculukAllView, CreateYolnYolcu, EkstraApiView

app_name = 'cars'
urlpatterns = [
    path('tr-booking/',CarCreate.as_view(),name="carcreate"),
    path('tr-booking/<int:pk>/',CarCreate.as_view(),name="carcreate1"),

    path('tr-booking-3/',YolcularAllview.as_view(),name="yolcular"),
    path('tr-booking-3/<int:pk>/',YolcularAllview.as_view(),name="yolcular1"),

    path('yolculuk/',YolculukAllView.as_view(),name="yolculuk"),
    path('yolculuk/<int:pk>/',YolculukAllView.as_view(),name="yolculuk1"),

    path('yolculuknyolcular/',CreateYolnYolcu.as_view(),name="createyny"),
    path('yolculuknyolcular//<int:pk>/',CreateYolnYolcu.as_view(),name="createyny1"),

    path('tr-booking-2/',EkstraApiView.as_view(),name="ekstra"),
    path('tr-booking-2/<int:pk>/',EkstraApiView.as_view(),name="ekstra1")



  
    


]