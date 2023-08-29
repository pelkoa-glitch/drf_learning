
from django.contrib import admin
from django.urls import path, include
from guitars.views import GuitarsViewSet
from rest_framework import routers


# Как работает роутер под капотом.
# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(
#             url=r'^{prefix}$',
#             mapping={'get': 'list'},
#             name='{basename}-list',
#             detail=False,
#             initkwargs={'suffix': 'List'}),
#         routers.Route(
#             url=r'^{prefix}/{lookup}$',
#             mapping={'get': 'retrieve'},
#             name='{basename}-detail',
#             detail=True,
#             initkwargs={'suffix': 'Detail'}),
#     ]


router = routers.DefaultRouter()
# Если из ViewSet убираем атрибут queryset,
# в роутере необходимо указать basename.
router.register(r'guitars', GuitarsViewSet, basename='guitars')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),  # http://127..0.0.1:8000/api/v1/guitars/
    # path('api/v1/guitarslist/', GuitarsViewSet.as_view({'get': 'list'})),
    # path('api/v1/guitarslist/<int:pk>/', GuitarsViewSet.as_view({'put': 'update'})),

]
