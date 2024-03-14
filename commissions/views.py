from django.shortcuts import render
from .models import Commission, Comment

def commissions_list(request):
    commissions = Commission.objects.order_by('created_on')
    ctx = {
        'commissions' : commissions
    }
    return render(request, "commissions_list.html", ctx)

def commission(request, pk):
    commissionName = Commission.objects.get(pk = pk)
    Comment = Comment.objects.filter(recipe__name=recipeName)
    ctx = {
         'comments' : Comment   
    }
    return render(request, "commission.html", ctx)
# Create your views here.
