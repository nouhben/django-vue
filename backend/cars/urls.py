
from django.urls import path
from .views import CarsViewSet #index
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cars',CarsViewSet)
urlpatterns = router.urls

# urlpatterns = [
#     path('cars/', index, name='home'),
# ]
