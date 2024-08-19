from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content  = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"