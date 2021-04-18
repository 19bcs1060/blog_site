from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse
# Create your views here.
def BlogView(request,blog_id,*args,**kwargs):
    obj= Blog.objects.get(id=blog_id)
    return HttpResponse(f"Hello {obj.content} ")