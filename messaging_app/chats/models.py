from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    # Extend this class later if needed
    pass


class Thread(models.Model):
    user1 = models.ForeignKey(CustomUser, related_name='thread_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(CustomUser, related_name='thread_user2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user1', 'user2']

    def __str__(self):
        return f"Thread between {self.user1.username} and {self.user2.username}"


class Message(models.Model):
    thread = models.ForeignKey(Thread, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"
