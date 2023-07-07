from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
#from rest_framework import permission
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    Permission_classes = [IsAuthenticated]

class BookingViewSet (viewsets.ModelViewSet):
    queryset = Bookingtable.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    Permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


