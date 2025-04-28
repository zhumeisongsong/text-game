from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TravelPlanViewSet

router = DefaultRouter()
router.register(r'plans', TravelPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 