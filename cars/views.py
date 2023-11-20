from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from cars.models import Car
from cars.forms import CarModelForm

def cars_view(request):
    cars = Car.objects.all().order_by('model')

    if 'search_model' in request.GET:
        search = request.GET.get('search_model')
        cars = Car.objects.filter(model__icontains=search)
        

    return render(
        request, 
        'cars_list.html', {
            'cars': cars
        }
    )


def new_car_view(request):
    
    if(request.method == 'POST'):
        new_car_form = CarModelForm(request.POST, request.FILES)
    
        if(new_car_form.is_valid()):
            new_car_form.save()
            messages.success(request, 'Carro Registrado com Sucesso!')
            return redirect('../cars_list')

    else:
        new_car_form = CarModelForm()
    return render (
        request,
        'new_car.html', {
            'new_car_form': new_car_form
        }
    )
    