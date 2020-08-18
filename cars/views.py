from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from cars.models import Car
from rest_framework.viewsets import ModelViewSet
from .serializers import CarSerializer
class CarsViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
# def index(request):
#     my_cars = Car.objects.all()
#     cars = []
#     for c in my_cars:
#         cars.append({
#             'name':c.name,
#             'age':c.age,
#             'car_id':c.car_id
#         }),

#     return JsonResponse(cars,safe=False)