from rest_framework import routers
from django.urls import path, include
from django.conf.urls.static import static
from . import views

router = routers.DefaultRouter()
router.register(r'',views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]