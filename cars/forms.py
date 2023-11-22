from django import forms
from cars.models import Brand, Car
import datetime


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if(value < 20000):
            self.add_error('value', 'O valor mínimo do carro deve ser R$20.000,00')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        current_year = today = datetime.date.today().year

        if((current_year - factory_year) > 50):
            self.add_error(
                'factory_year', f'O carro não pode ter mais de 50 anos (Ano Fabricação < {current_year - 50})')
        return factory_year

