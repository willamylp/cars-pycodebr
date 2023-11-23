from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view, new_car_view
from accounts.views import admin_register_view, user_register_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_register/', admin_register_view, name='admin_register'),
    path('user_register/', user_register_view, name='user_register'),
    path('login/', login_view, name='login'),
    path('cars_list/', cars_view, name='cars_list'),
    path('new_car/', new_car_view, name='new_car'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
