from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser


class Profile(models.Model):
    fullname    = models.CharField(max_length=250)
    email       = models.EmailField(unique=True)
    matricID    = models.CharField(max_length=50, unique=True)
    password    = models.CharField(max_length=5000)

    def save(self, *args, **kwargs):
        if not AbstractBaseUser.objects.filter(username=self.matricID).exists():
            instance = AbstractBaseUser.objects.create(username=self.matricID, email=self.email)
            instance.set_password(self.password)
            self.password = instance.set_password(self.password)

        super().save(*args, **kwargs)
