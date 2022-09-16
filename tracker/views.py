from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import transaction

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def addmoney(request):
    if request.method == 'POST':
        Transaction = transaction()
        Transaction.expense = request.POST['expense']
        Transaction.amount = request.POST['amount']
        Transaction.category = request.POST['category']
        Transaction.date = request.POST['date']
        Transaction.comment = request.POST['comment']     
        Transaction.transactor = request.user
        Transaction.save()
        
        if 'add' in request.POST:
            return HttpResponseRedirect(request.path_info)
        else:
            return redirect('/index/')
        



    else:
        return render(request, 'home/addmoney.html')


def info(request):
    return render(request, 'home/info.html')

def profile(request):
    return render(request, 'home/profile.html')

def weekly(request):
    return render(request, 'home/weekly.html')

def stats(request):
    return render(request, 'home/stats.html')

def charts(request):
    return render(request, 'home/charts.html')

def tables(request):
    return render(request, 'home/tables.html')