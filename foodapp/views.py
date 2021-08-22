from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Food
from .serializers import FoodSerializer

class FoodView(viewsets.ModelViewSet):
    queryset = Food.objects.all().order_by('-id')
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
