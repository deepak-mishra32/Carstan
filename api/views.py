from rest_framework.views import APIView
from rest_framework.response import Response
from cars.models import CarDetail
from api.serializers import CarDetailSerializers
from rest_framework import status

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
        # cars= CarDetail.objects.all()
        # print(type)
        cars= CarDetail.objects.all().filter(name=name)
        serializer = CarDetailSerializers(cars,many=True)
        # print(serializer.data)
        return Response(serializer.data)