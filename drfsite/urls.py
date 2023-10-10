from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from guitars.views import GuitarsAPIList, GuitarsAPIUpdate, GuitarsAPIDestroy


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
