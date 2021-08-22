from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Food(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food', null=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    products_list = models.TextField()
    quantity = models.IntegerField()
    image = models.URLField()

    def __str__(self):
        return self.title