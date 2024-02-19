from django.shortcuts import render,redirect
import numpy as np
import pandas as pd
import math
import datetime as dt
import time
import yfinance as yf
import seaborn as sns
from pylab import mpl,plt
from accounts.models import Staff
from .models import Invest

from django.core.exceptions import ValidationError, ObjectDoesNotExist
from openpyxl import Workbook
from django.http import HttpResponse
# Create your views here.
data1={}
def home(request):
    data=[]
    stock_symbol = ['AAPL','AMZN','TSLA','GOOG','NFLX']
    for symbol in stock_symbol:
        ticker = yf.Ticker(symbol)
        live_data = ticker.history(period='1d')
        print(live_data)
        data=live_data.values.tolist()
        data1[symbol]={
            'open': round(data[0][0], 2),
            'high': round(data[0][1], 2),
            'low':round(data[0][2], 2),
            'close':round(data[0][3], 2),
            'volume':round(data[0][4], 2),
            'div':round(data[0][5], 2),
           'stk_spl':round(data[0][6], 2),
        }
   #print(data1['AAPL'])
    portfolio=portfolio1(request)
    print(portfolio)
    return render(request, 'investment/investments.html', {'data': data1,'portfolio':portfolio})

def create(request):
    tid = Invest.objects.all().order_by('-id').first()
    trid=int(str(tid))+1
    print(trid)
    
    if not data1:
        data=[]
        stock_symbol = ['AAPL','AMZN','TSLA','GOOG','NFLX']
        for symbol in stock_symbol:
            ticker = yf.Ticker(symbol)
            live_data = ticker.history(period='1d')
            print(live_data)
            data=live_data.values.tolist()
            data1[symbol]={
                'open': round(data[0][0], 2),
                'high': round(data[0][1], 2),
                'low':round(data[0][2], 2),
                'close':round(data[0][3], 2),
                'volume':round(data[0][4], 2),
                'div':round(data[0][5], 2),
            'stk_spl':round(data[0][6], 2),
            }
    if request.method=='POST':
        account=Staff.objects.get(user=request.user)
        symbol=request.POST['symbol']
        date=request.POST['date']
        shares=request.POST['item_name_0']
        spot_price=request.POST['item_money_change_0']
        total_amount=request.POST['total_cost_0']
        new_investment = Invest(account=account, symbol=symbol, total_amount=total_amount, date=date,
                              shares=shares, spot_price=spot_price)
        new_investment.save()
        print(account," ",symbol," ",date," ",shares," ",spot_price," ",total_amount)
        return redirect('/investment/home/')
    return render(request,'investment/create.html',{'data': data1,'tid':trid})

def portfolio1(request):
    data={}
    data2=[]
    data1 = Invest.objects.all()
    for obj in data1:
        str2=str(obj.account)
        str1=str(request.user)
        if str1==str2:
            data2.append(obj)
    return data2

def details(request, invest_id):
    # If table_id is invalid...
    try:
        invest = Invest.objects.get(id=invest_id)
    except ValidationError:
        return custom_error_404(request, data)
    except ObjectDoesNotExist:
        return custom_error_404(request, data)

    #data= invest_record
    #data['items'] = invest_record.items.all()
    return render(request, 'investment/details.html', {'invest': invest})

def export_to_excel(request):
    # Query your data from the database (replace YourModel with your actual model)
    data = Invest.objects.all()

    # Create a workbook and add a worksheet
    workbook = Workbook()
    worksheet = workbook.active

    # Write headers to the worksheet (replace 'field1', 'field2', etc. with your actual field names)
    headers = ['Symbol', 'Shares', 'Spot Price','Total Amount','Date']
    worksheet.append(headers)

    # Write data to the worksheet
    for row in data:
        str2=str(row.account)
        str1=str(request.user)
        if str1==str2: 
            row_data = [row.symbol, row.shares, row.spot_price,row.total_amount,row.date]  # Replace with your actual field names
            worksheet.append(row_data)

    # Create a response with the appropriate content type for Excel files
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=exported_data.xlsx'

    # Save the workbook to the response
    workbook.save(response)

    return response