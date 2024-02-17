from django.shortcuts import render, HttpResponse, redirect
from rail_ticket_app.models import Train

# Create your views here.



def home(request):
       print("Method is",request.method)
       if request.method =="GET":
            return render(request,'index.html')
       else:
              #return HttpResponse("insert data into DB")
            n=request.POST['name']
            print("Name is",n)
       return HttpResponse("Values fetched successfully")
  
def search(request):
     fromStation=request.GET['fromStn']
     toStation=request.GET['toStn']
     t=Train.objects.filter(source=fromStation,destination=toStation)
     print(t)
     context={}
     context['trains']=t
     return render(request,'show_train.html',context)
     

def check_PNR(request):
     return render(request,'pnr.html')

def chart(request):
     return render(request,'reservation_chart.html')

def ticket_details(request):
     return HttpResponse("ok")
     
# Create your views here.
