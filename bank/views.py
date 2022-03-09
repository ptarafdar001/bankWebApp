from django.shortcuts import render, get_object_or_404
from .models import Accounts, Transactions

# Create your views here.


def home(request):
    return render(request, 'home.html')


def accounts(request, msg=""):
    allAccounts = Accounts.objects.all()
    return render(request, 'accounts.html', {'data': allAccounts, 'msg': msg})


def transactions(request, msg=""):
    allTransactions = Transactions.objects.all()
    return render(request, 'transactions.html', {'data': allTransactions, 'msg': msg})


def new(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        balance = request.POST.get('balance')
        check = request.POST.get('check')
        if(check):
            items = Accounts.objects.all()
            no = len(items)
            account = Accounts()
            account.name = name
            account.email = email
            account.balance = balance
            account.accountNo = 3312451 + 1 + no
            account.save()
            return accounts(request, "Account Created.")

    else:
        return render(request, 'new.html')


def transfer(request, id):
    if request.method == 'POST':
        account = request.POST.get('account')
        amount = request.POST.get('amount')
        accountTo = get_object_or_404(Accounts, accountNo=account)
        accountFrom = get_object_or_404(Accounts, id=id)
        if accountFrom.balance >= int(amount) and accountFrom.accountNo != accountTo.accountNo:
            accountTo.balance += int(amount)
            accountFrom.balance -= int(amount)
            transaction = Transactions()
            transaction.toAcc = accountTo.name
            transaction.fromAcc = accountFrom.name
            transaction.balance = amount
            transaction.success = True
            transaction.save()
            accountFrom.save()
            accountTo.save()
            return transactions(request, "Transfer Successfull.")
        else:
            transaction = Transactions()
            transaction.toAcc = accountTo.name
            transaction.fromAcc = accountFrom.name
            transaction.balance = amount
            transaction.success = False
            transaction.save()
            return transactions(request, "Transfer Failed.")

    else:
        obj = get_object_or_404(Accounts, id=id)
        data = Accounts.objects.all()
        return render(request, 'transfer.html', {'item': obj, 'data': data})
