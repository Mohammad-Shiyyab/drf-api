from django.shortcuts import render
from .models import Thing
from rest_framework.generics import ListAPIView , RetrieveAPIView , ListCreateAPIView
from .serializers import ThingSerializer

from .serializers import ThingSerializer
# Create your views here.


class ThingListView(ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetailView(RetrieveAPIView):  
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer  