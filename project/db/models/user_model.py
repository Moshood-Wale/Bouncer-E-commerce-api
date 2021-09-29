from django.db import models
import uuid


class User(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.EmailField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    otp_code = models.CharField(default=None, max_length=6, unique=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s, %s' % (self.first_name, self.last_name)

