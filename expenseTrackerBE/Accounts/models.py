from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, BaseUserManager

# User manager
class UserManager:
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

# User model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    user_agreement = models.BooleanField(default=False)
    USERNAME_FIELD = "email"

    objects = UserManager()
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "user_agreement"]



    def __str__(self):
        return self.email

