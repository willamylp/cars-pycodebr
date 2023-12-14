from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from cars.models import Car, CarInvetory
import os
from app import settings
# from openai_api.client import get_car_ai_bio

def car_invetory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']

    CarInvetory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_invetory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_invetory_update()


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not(instance.bio):
        # ai_bio = get_car_ai_bio(
        #     instance.model, instance.brand, instance.model_year
        # )
        
        #instance.bio = ai_bio

        instance.bio = "Biografia não informada!"

@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    if instance.photo:
        file_path = os.path.join(settings.MEDIA_ROOT, str(instance.photo))
        if os.path.exists(file_path):
            os.remove(file_path)
