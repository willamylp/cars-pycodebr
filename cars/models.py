from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Nome da Marca", max_length=200)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(verbose_name="Modelo", max_length=200)
    brand = models.ForeignKey(Brand, verbose_name="Marca", on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(verbose_name="Ano Fabricação", blank=True, null=True)
    model_year = models.IntegerField(verbose_name="Ano Modelo", blank=True, null=True)
    plate = models.CharField(verbose_name="Placa", max_length=10, blank=True, null=True)
    value = models.FloatField(verbose_name="Valor", blank=True, null=True)
    photo = models.ImageField(verbose_name="Foto", upload_to='cars/', blank=True, null=True)
    bio = models.TextField(verbose_name="Bio do Carro", blank=True, null=True, max_length=250)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f"{self.brand.name} | {self.model}"
    

class CarInvetory(models.Model):
    cars_count = models.IntegerField(verbose_name="Carros em Estoque")
    cars_value = models.FloatField(verbose_name="Valor Total em Estoque")
    created_at = models.DateTimeField(verbose_name="Data de Registro", auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.cars_count} - R$ {self.cars_value:, .2f}"
    
        