from django.shortcuts import render
from django.http import JsonResponse
from .models import BlogPost
from django.core.serializers import serialize

# Create your views here.
def index(request):
    return render(request, 'tasks/post_list.html')