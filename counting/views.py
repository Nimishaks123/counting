from  django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')
def count(request):
    stripped_str=request.GET.get('nimisha', '').strip()
    print("stripped_str",stripped_str.split(' '))
    str_len = len(stripped_str.split(' '))
    return HttpResponse(f"{stripped_str} {str_len}")