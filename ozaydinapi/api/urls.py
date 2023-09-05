from django.urls import path, include
# lookup field vermezsek auto pk olarak geliyo 
from .views import CarCreate,  YolcularAllview, YolculukAllView, CreateYolnYolcu, EkstraApiView

app_name = 'cars'
urlpatterns = [
    path('create/',CarCreate.as_view(),name="carcreate"),
    path('create/<int:pk>/',CarCreate.as_view(),name="carcreate1"),

    path('yolcular/',YolcularAllview.as_view(),name="yolcular"),
    path('yolcular/<int:pk>/',YolcularAllview.as_view(),name="yolcular1"),

    path('yolculuk/',YolculukAllView.as_view(),name="yolculuk"),
    path('yolculuk/<int:pk>/',YolculukAllView.as_view(),name="yolculuk1"),

    path('yolculuknyolcular/',CreateYolnYolcu.as_view(),name="createyny"),
    path('yolculuknyolcular//<int:pk>/',CreateYolnYolcu.as_view(),name="createyny1"),

    path('ekstra/',EkstraApiView.as_view(),name="ekstra"),
    path('ekstra/<int:pk>/',EkstraApiView.as_view(),name="ekstra1")



  
    


]