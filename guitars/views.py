from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Guitars
from .permissions import IsAdminOrReadOnly
from .serializers import GuitarsSerializer


class GuitarsAPIList(generics.ListCreateAPIView):
    queryset = Guitars.objects.all()
    serializer_class = GuitarsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class GuitarsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Guitars.objects.all()
    serializer_class = GuitarsSerializer
    permission_classes = (IsAuthenticated, )


class GuitarsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Guitars.objects.all()
    serializer_class = GuitarsSerializer
    permission_classes = (IsAdminOrReadOnly, )
