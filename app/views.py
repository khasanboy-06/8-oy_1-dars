from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import CarsInfo
from .serializers import CarsSerializer
from rest_framework import generics


class CarsAPIView(generics.ListAPIView):
    queryset = CarsInfo.objects.all()
    serializer_class = CarsSerializer



class CarsAPIDetailView(RetrieveAPIView):
    queryset = CarsInfo.objects.all()
    serializer_class = CarsSerializer