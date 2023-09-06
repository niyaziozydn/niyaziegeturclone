from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView, DestroyAPIView, CreateAPIView, GenericAPIView, ListCreateAPIView
from ozaydinapi.models import  Cars, Ekstra, NeredenNereye, YolcuLast
from .serializers import CarsSerializer,YolcuLastSerializer, NeredenNereyeSerializer,YolcubilgiSerializer, EkstraSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework import status

class CarCreate(CreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

class NeredenNereyeApiView(APIView):

    def post(self, request, format=None):
        serializer = NeredenNereyeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EkstraApiview(APIView):

    def post(self, request, format=None):
        serializer = EkstraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class YolcuBilgiApiView(APIView):

    def post(self, request, format=None):
        serializer = YolcubilgiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       
      
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class YolcuLasApiView(APIView):
    def post(self, request, format=None):
        serializer = YolcuLastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       
      
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserList(APIView):
    def post(self,request):
        data = {}
        Yolculast = YolcuLast.objects.all()
        for x in Yolculast:
            data["Nereden"] = x.neredennereye.Nereden
            data["Nereye"] = x.neredennereye.Nereye
            data["Yolcu"] = x.neredennereye.Yolcu
            data["CarInfo"] = {"Cartitle": x.neredennereye.car.Cartitle,
                               "CarType": x.neredennereye.car.Cartype,
                               "CarFiyat":x.neredennereye.car.Carfiyat,
                               }
            data["Ekstralar"] = {"Köprü":x.yolcubilgi.ekstra.Kopru,
                                 "Bebek Koltuğu":x.yolcubilgi.ekstra.Bebekkoltuk,
                                 "Yüksek Koltuk":x.yolcubilgi.ekstra.Yuksekkoltuk,
                                 "saat Ekstrası":x.yolcubilgi.ekstra.saatekstra,}
            data["Yolcu Bilgileri"] = {"isim":x.yolcubilgi.isim,
                                       "Soy isim": x.yolcubilgi.soyisim,
                                       "Yaş":x.yolcubilgi.yas,
                                       "Uyruğu":x.yolcubilgi.uyruk,
                                       "Ek bilgi":x.yolcubilgi.ekbilgi}
  


        return Response(data)




