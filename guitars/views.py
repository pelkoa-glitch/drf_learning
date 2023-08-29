from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Guitars, Category
from .serializers import GuitarsSerializer


class GuitarsViewSet(viewsets.ModelViewSet):
    # Если убираем атрибут queryset в
    # роутере необходимо добавить basename
    # queryset = Guitars.objects.all()
    serializer_class = GuitarsSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Guitars.objects.all()

        return Guitars.objects.filter(pk=pk)

    # С помощью декоратора @action можно добавлять новые "не стандартные
    # маршруты" в класс ViewSet
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})


# # Api на основе базовых классов DRF
# class GuitarsAPIList(generics.ListCreateAPIView):
#     queryset = Guitars.objects.all()
#     serializer_class = GuitarsSerializer
#
#
# class GuitarsAPIUpdate(generics.UpdateAPIView):
#     queryset = Guitars.objects.all()
#     serializer_class = GuitarsSerializer
#
#
# class GuitarsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Guitars.objects.all()
#     serializer_class = GuitarsSerializer


# Как работает Api под капотом(GET, POST, PUT, DELETE).
# class GuitarsAPIView(APIView):
#     def get(self, request):
#         entry_list = Guitars.objects.all()
#         return Response({'posts': GuitarsSerializer(entry_list, many=True).data})
#
#     def post(self, request):
#         serializer = GuitarsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'title': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Guitars.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does noe exist"})
#
#         serializer = GuitarsSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = Guitars.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error": "Object does not exists"})
#
#         return Response({"post": "delete post " + str(pk)})
