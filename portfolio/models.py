from django.db import models
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin,HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content  = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"
    

    
class Team(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Team/images')
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Project(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content  = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"
    

    
class About(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content  = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"
    

    
def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

def __str__(self):
    return f"{self.title} by {self.author}"