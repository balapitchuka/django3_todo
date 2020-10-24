from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.todo



