from rest_framework.views import APIView
from rest_framework.response import Response
from cars.models import CarDetail
from api.serializers import CarDetailSerializers
from rest_framework import status
from django.db.models import Count

class CarDetailAPIView(APIView):

    def get(self, request):
        cars= CarDetail.objects.all()
        serializer = CarDetailSerializers(cars, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CarDetailSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AllCarDetailView(APIView):

    def get_object(self,id):
        try:
            return CarDetail.objects.get(id=id)
        except CarDetail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        cars= self.get_object(id)
        if cars is not None:
            serializer=CarDetailSerializers(cars)
            return Response(serializer.data)
        return Response("Not Such Data",status=status.HTTP_404_NOT_FOUND)

    def put(self,request,id):
        cars= self.get_object(id)
        serializer = CarDetailSerializers(cars,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        cars= self.get_object(id)    
        cars.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductDetailView(APIView):

    def get(self, request,name):
        try:
            cars = CarDetail.objects.get(name__istartswith=name)
            serializer = CarDetailSerializers(cars)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":f"Not Data Found For {name}"},status=status.HTTP_404_NOT_FOUND)

class CompanyProductView(APIView):

    def get(self, request,company):
        try:
            cars = CarDetail.objects.all().filter(company__istartswith=company)
            serializer = CarDetailSerializers(cars,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":f"Not Data Found For {company}"},status=status.HTTP_404_NOT_FOUND)

class CarTypeView(APIView):

    def get(self, request,type):
        try:
            cars = CarDetail.objects.all().filter(car_type__icontains=type)
            serializer = CarDetailSerializers(cars,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":f"Not Data Found For {type}"},status=status.HTTP_404_NOT_FOUND)

class PriceView(APIView):

    def get(self, request,price):
        try:
            cars = CarDetail.objects.all().filter(price__lte=price)
            serializer = CarDetailSerializers(cars,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":f"Not Data Found For {price}"},status=status.HTTP_404_NOT_FOUND)

class TransmissionTypeView(APIView):

    def get(self, request,type):
        try:
            cars = CarDetail.objects.all().filter(transmission_type__icontains=type)
            serializer = CarDetailSerializers(cars,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":f"Not Data Found For {type}"},status=status.HTTP_404_NOT_FOUND)

class FilterView(APIView):

    def get(self, request,type,category,company,price,fuel):
        try:
            cars = CarDetail.objects.all().filter(transmission_type__icontains=type).filter(company__icontains=company).filter(car_type__icontains=category).filter(price__lte=price).filter(fuel_type__icontains=fuel)
            serializer = CarDetailSerializers(cars,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":f"Not Data Found For {type},{category},{fuel},{price} and {company}"},status=status.HTTP_404_NOT_FOUND)                        