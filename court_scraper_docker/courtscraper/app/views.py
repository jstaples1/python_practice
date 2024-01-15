from django.shortcuts import render
from django.utils.safestring import mark_safe

from app import functions

# Create your views here.

from django.shortcuts import render

def court_view(request):
  
  date = request.GET.get('date')
  #courtNumber = request.GET.get('courtNumber')

  
  context = {
        "title" : "Court",
        "body" : mark_safe(functions.getResponseBodies(date)) 

       
  
  }
  
  return render(request, "court.html", context)
  
         
    


