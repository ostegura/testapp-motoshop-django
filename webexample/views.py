from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("<h3> Learning Django in a few days, kappa</h3>")