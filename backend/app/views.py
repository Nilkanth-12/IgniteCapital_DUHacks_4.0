from django.http import JsonResponse
from .models import startups_collection, investors_collection

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
    startups = [
        {"name": "TechX", "industry": "AI", "funding": "$1M"},
        {"name": "EcoGreen", "industry": "Sustainability", "funding": "$500K"},
        {"name": "HealthSync", "industry": "Healthcare", "funding": "$750K"},
    ]

    investors = [
        {"name": "John Doe", "investment": "$5M"},
        {"name": "Jane Smith", "investment": "$2M"},
        {"name": "Mark Lee", "investment": "$3M"},
    ]

    return render(request, "home.html", {"startups": startups, "investors": investors})

