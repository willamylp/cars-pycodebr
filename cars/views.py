from django.shortcuts import render
from django.http import HttpResponse
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all().order_by('model')

    if 'search_model' in request.GET:
        search = request.GET.get('search_model')
        cars = Car.objects.filter(model__icontains=search)
        

    return render(
        request, 
        'cars.html', {
            'cars': cars
        }
    )
