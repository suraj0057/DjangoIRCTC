from django.contrib import admin
from django.urls import path 
from rail_ticket_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('pnr',views.check_PNR),
    path('chart',views.chart),
    path('search',views.search),
    path('book_now',views.book_ticket),
    path('book_ticket',views.book_ticket),
    path('test',views.test),
]

