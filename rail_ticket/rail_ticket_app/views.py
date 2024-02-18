from django.shortcuts import render, HttpResponse, redirect
from rail_ticket_app.models import Train
from django.contrib.auth.models import User

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
     j=request.GET['journeyDate']
     print(t)
     context={}
     context['fromStn']=fromStation
     context['toStn']=toStation
     context['trains']=t
     context['journeyDate']=j
     context['selectedClass']=''
     return render(request,'show_train.html',context)
     

def check_PNR(request):
     return render(request,'pnr.html')

def chart(request):
     return render(request,'reservation_chart.html')

def ticket_details(request):
     return HttpResponse("ok")

def selectedClass(request,classtype, price):
     context={}
     return render(request,'show_train.html',context)

def book_ticket(request):
     context={}
     seletedClass=request.POST['seletedClass']
     trainContext=request.POST['trainContext']
     arrivalTime=request.POST['arrivalTime']
     sourceStn=request.POST['sourceStn']
     destStn=request.POST['destStn']
     jDate=request.POST['jDate']
     context['seletedClass']=seletedClass
     context['trainContext']=trainContext
     context['arrivalTime']=arrivalTime
     context['sourceStn']=sourceStn
     context['destStn']=destStn
     context['jDate']=jDate
     return render(request,'book_ticket.html',context)
    # else:          
     #     return redirect('/user_login')
     
# Create your views here.
