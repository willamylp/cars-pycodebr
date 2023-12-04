from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from cars.models import Car
from cars.forms import CarModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class CarsListView(ListView):
    model = Car
    template_name = 'cars_list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search_model')

        if search:
            cars = cars.filter(model__icontains=search)

        return cars


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars_list/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    
    def get_success_url(self):
        return reverse_lazy(
            'car_detail',
            kwargs={'pk': self.object.pk}
        )


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    def get(self, request, pk):
        object = get_object_or_404(Car, pk=pk)
        object.delete()
        messages.success(request, 'Carro Deletado com Sucesso!')
        return redirect('cars_list')


