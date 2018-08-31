from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'mainApp/homePage.html')

def contact(request):
	return render(request, 'mainApp/basic.html', {'values': ['If you have any questions, ask me by the phone numbers:', 
															'(099) 099-99-99 - Sasha', '(088) 088-88-88 - Dasha', 
															'(077) 077-77-77 - Natasha', 'whatagreatemail@gmail.com']})