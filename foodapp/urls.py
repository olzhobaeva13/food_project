from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import FoodView

router = SimpleRouter()
router.register('foodapp', FoodView)
urlpatterns = []

urlpatterns += router.urls