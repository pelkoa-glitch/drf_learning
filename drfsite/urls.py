from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from guitars.views import GuitarsAPIList, GuitarsAPIUpdate, GuitarsAPIDestroy

# from guitars.views import GuitarsViewSet # Импорт для использования ViewSet
# from rest_framework import routers # Импорт для использования роутера

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/guitars/', GuitarsAPIList.as_view()),
    path('api/v1/guitars/<int:pk>/', GuitarsAPIUpdate.as_view()),
    path('api/v1/guitarsdelete/<int:pk>/', GuitarsAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
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


# router = routers.DefaultRouter()
# Если из ViewSet убираем атрибут queryset,
# в роутере необходимо указать basename.
# router.register(r'guitars', GuitarsViewSet, basename='guitars')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include(router.urls)),  # http://127..0.0.1:8000/api/v1/guitars/
#     path('api/v1/guitarslist/', GuitarsViewSet.as_view({'get': 'list'})),
#     path('api/v1/guitarslist/<int:pk>/', GuitarsViewSet.as_view({'put': 'update'})),
#
# ]
