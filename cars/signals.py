from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from cars.models import Car, CarInvetory


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
    pass


@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    pass