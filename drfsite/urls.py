
from django.contrib import admin
from django.urls import path
from guitars.views import GuitarsAPIList, GuitarsAPIUpdate, GuitarsAPIDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/guitarslist/', GuitarsAPIList.as_view()),
    path('api/v1/guitarslist/<int:pk>/', GuitarsAPIUpdate.as_view()),
    path('api/v1/guitarsdetail/<int:pk>/', GuitarsAPIDetailView.as_view())
]
