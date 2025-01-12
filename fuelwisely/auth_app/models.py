from django.db import models

class UserProfile(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def str(self):
        return self.name