
from django.contrib import admin
from django.urls import path, include
from guitars.views import GuitarsViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'guitars', GuitarsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),  # http://127..0.0.1:8000/api/v1/guitars/
    # path('api/v1/guitarslist/', GuitarsViewSet.as_view({'get': 'list'})),
    # path('api/v1/guitarslist/<int:pk>/', GuitarsViewSet.as_view({'put': 'update'})),

]
