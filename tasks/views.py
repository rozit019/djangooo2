from django.shortcuts import render
from django.http import JsonResponse
from .models import BlogPost
from django.core.serializers import serialize
import json

# Create your views here.
def index(request):
    return render(request, 'tasks/post_list.html')

def get_posts(request):
    #
    posts = BlogPost.objects.all().order_by('-published')
    #saves the data from the admin site in following format
    data = [{
        'title':post.title,
        'content': post.content,
        'published': post.published.strftime('%Y-%m-%d %H:%M:%S'),#date time save grna
    }for post in posts] #hamle backend bata fetch grera layeko data lai list ma rakhyo
    
    return JsonResponse(data, safe=False)  # safe=False allows non-dict objects to be serialized