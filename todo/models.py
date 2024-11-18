from django.conf import settings
from django.db import models


class Todo(models.Model):
    content = models.CharField(max_length=100)
    due_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
