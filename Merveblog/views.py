from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    gonderiler=Post.objects.all().order_by('created_date')
    return render(request, r'Merveblog/post_list.html', {'posts':gonderiler})
