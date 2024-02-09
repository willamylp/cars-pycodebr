from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsListView, NewCarCreateView, CarDetailView, CarUpdateView, CarDeleteView
from accounts.views import admin_register_view, user_register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('admin_register/', admin_register_view, name='admin_register'),
    path('user_register/', user_register_view, name='user_register'),
    path('', login_view),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('cars_list/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),
    path('car_detail/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car_update/<int:pk>/', CarUpdateView.as_view(), name='car_update'),
    path('car_delete/<int:pk>/', CarDeleteView.as_view(), name='car_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
