from django.urls import path,include
from .import views

urlpatterns = [
    path('menu/',views.menu,name='menu'),
    path("add/",views.add_menu,name='add_menu'),
    path("remove/<int:dish_id>/", views.remove_menu, name='remove_menu'),
    path("update_availability/<int:dish_id>/", views.update_availability, name='update_availability')
]