from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bookmark_list(request):
    return render(request, "bookmark/list.html")

def bookmark(request, number):
     return  render(request, "bookmark_detail.html", {"number": number})
def bookmark_detail(request, number):
    context = {"number": number}
    return render(request,"bookmark_detail", "context")
