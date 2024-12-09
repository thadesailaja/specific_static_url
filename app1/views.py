from django.shortcuts import render

# Create your views here.
def staticurl(request):
    return render(request,'nature.html')