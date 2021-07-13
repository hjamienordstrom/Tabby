from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'about.html')

def about(request):
  return render(request, 'about.html')

def trips_detail(request, trip_id):
   return render(request, 'trips/detail.html')