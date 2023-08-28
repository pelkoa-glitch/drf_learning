
from django.contrib import admin
from django.urls import path
from guitars.views import GuitarsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/guitarslist', GuitarsAPIView.as_view()),
    path('api/v1/guitarslist/<int:pk>/', GuitarsAPIView.as_view()),
]
