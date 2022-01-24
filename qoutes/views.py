from cmath import log
from django.contrib import messages
from django.shortcuts import render ,redirect
import requests
import json

from qoutes.models import Ticker

from .forms import StockForm

# Create your views here.

def home(request):
    

    if request.method=="POST":
        ticker=request.POST['ticker']
        api_request= requests.get('https://cloud.iexapis.com/stable/stock/'+ticker+'/quote?token=pk_cb27bba1e56b48cea69bd2a322ab8e4c')

       
        try:
            api=json.loads(api_request.content)
       

        except Exception as e:
            api="Error..."
        #print(api)
        
        return render(request,"home.html",{'api':api})

    else:
     return render(request,"home.html",{"ticker":"Enter any ticker"})    

    


def about(request):

    return render(request,"about.html",{})

def stock_data(request):
    if request.method=="POST":
        form=StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,("Stcok Has been added")) 
            return redirect("stock_data")
    ticker=Ticker.objects.all()
    output=[]
    for ticke_item in ticker:
        
        api_request= requests.get('https://cloud.iexapis.com/stable/stock/'+str(ticke_item)+'/quote?token=pk_cb27bba1e56b48cea69bd2a322ab8e4c')
       
        try:
            api=json.loads(api_request.content)
            output.append(api)
        except Exception as e:
            api="Error..."
            
    mylist = zip(output,ticker)
    context={
        "mylist":mylist
    }     
    return render(request,"stock_data.html",context)


def delete_stock(request,stock_id):
    item =Ticker.objects.get(pk=stock_id)
    item.delete()
    messages.success(request,("Item has been Deleted"))
    return redirect('stock_data')