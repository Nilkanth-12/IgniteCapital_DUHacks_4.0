from django.http import JsonResponse
from .models import startups_collection, investors_collection

# Get all Startups
def startup_list(request):
    startups = list(startups_collection.find({}, {"_id": 0}))  
    return JsonResponse({'startups': startups})

# Get all Investors
def investor_list(request):
    investors = list(investors_collection.find({}, {"_id": 0}))  
    return JsonResponse({'investors': investors})
