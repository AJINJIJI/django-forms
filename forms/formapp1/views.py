from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")



def data(request):
    name=request.POST['Firstname']
    age=request.POST['yourage']
    print(name,age)
    return render(request,"details.html",{"one":name,"two":age})
