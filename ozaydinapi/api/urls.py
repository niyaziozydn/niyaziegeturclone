from django.urls import path, include
# lookup field vermezsek auto pk olarak geliyo 
from .views import NeredenNereyeApiView, CarCreate, YolcuLasApiView,UserList,EkstraApiview, YolcuBilgiApiView
app_name = 'cars'
urlpatterns = [
    path('trbooking/',NeredenNereyeApiView.as_view(),name="neredennereye"),
    path('trbooking2/',EkstraApiview.as_view(),name="ekstra1"),
    path('trbooking3/',YolcuBilgiApiView.as_view(),name="ekstra2"),
    path('trbooking4/',YolcuLasApiView.as_view(),name="ekstra3"),
    path('trbooking5/',UserList.as_view(),name="ekstra4"),




    path('carcreate/',CarCreate.as_view(),name="carcreate"),
    path('trbooking/<int:pk>/',NeredenNereyeApiView.as_view(),name="neredennereye"),









  
    


]
  
    


