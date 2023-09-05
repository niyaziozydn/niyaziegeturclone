from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView, DestroyAPIView, CreateAPIView, GenericAPIView, ListCreateAPIView
from ozaydinapi.models import Cars, Yolcular,Yolculuk,YolculuknYolcular, Ekstra
from .serializers import CarsSerializer, YolcularSerializer, YolculukSerializer, YolculuknYolcularSerializer, EkstraSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework import status

class CarCreate(APIView):
    def get(self, request, pk=None):  # Add 'pk=None' to the get method
        if pk is not None:
            book = Cars.objects.get(pk=pk)
            serializer = CarsSerializer(book)
            return Response(serializer.data)
        else:
            books = Cars.objects.all()
            serializer = CarsSerializer(books, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = Cars.objects.get(pk=pk)
            serializer = CarsSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid book ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = Cars.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = Cars.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        


class YolcularAllview(APIView):
    def get(self, request, pk=None):  # Add 'pk=None' to the get method
        if pk is not None:
            book = Yolcular.objects.get(pk=pk)
            serializer = YolcularSerializer(book)
            return Response(serializer.data)
        else:
            books = Yolcular.objects.all()
            serializer = YolcularSerializer(books, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = YolcularSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = Yolcular.objects.get(pk=pk)
            serializer = YolcularSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid book ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = Yolcular.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = Yolcular.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class YolculukAllView(APIView):

    def get(self, request, pk=None):  # Add 'pk=None' to the get method
        if pk is not None:
            book = Yolculuk.objects.get(pk=pk)
            serializer = YolculukSerializer(book)
            return Response(serializer.data)
        else:
            books = Yolculuk.objects.all()
            serializer = YolculukSerializer(books, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = YolculukSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = Yolculuk.objects.get(pk=pk)
            serializer = YolculukSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid book ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = Yolculuk.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = Yolculuk.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class CreateYolnYolcu(APIView):
    def get(self, request, pk=None):  # Add 'pk=None' to the get method
        if pk is not None:
            book = YolculuknYolcular.objects.get(pk=pk)
            serializer = YolculuknYolcularSerializer(book)
            return Response(serializer.data)
        else:
            books = YolculuknYolcular.objects.all()
            serializer = YolculuknYolcularSerializer(books, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = YolculuknYolcularSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = YolculuknYolcular.objects.get(pk=pk)
            serializer = YolculuknYolcularSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid book ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = YolculuknYolcular.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = YolculuknYolcular.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)














class EkstraApiView(APIView):

    def get(self, request, pk=None):  # Add 'pk=None' to the get method
        if pk is not None:
            book = Ekstra.objects.get(pk=pk)
            serializer = EkstraSerializer(book)
            return Response(serializer.data)
        else:
            books = Ekstra.objects.all()
            serializer = EkstraSerializer(books, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = EkstraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = Ekstra.objects.get(pk=pk)
            serializer = EkstraSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid book ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = Ekstra.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = Ekstra.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
