from django.db import models

# Create your models here.
class Blog(models.Model):
    content=models.TextField(blank=True,null=True)
    content_title=models.TextField(blank=True,null=True)
    image= models.FileField(upload_to='images',blank=True)
    