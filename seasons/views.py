from django.shortcuts import render
from django.http import HttpResponse
from home.models import *

# Create your views here.
def seasons(request):
    seasons = seasonsTbl.objects.all()
    return render(request, 'seasons/seasonshome.html', {"seasons":seasons})

def seasonview(request, usrseason):
    stats = statsTbl.objects.all().filter(season=usrseason)
    matches = matchesTbl.objects.all().filter(season=usrseason)
    context = {"stats": stats, "matches": matches}
    if usrseason == "2017-2018":
        return render(request, 'seasons/20172018page.html', context)
    else:
        return render(request, 'seasons/nomissingdata.html', context)