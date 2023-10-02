from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home_page, name = "home"),
    path('login/', login_view, name="login"),
    path('register/', registration_view, name="register"),
    path('landing-page/', landing_page, name="landing-page"),
    path('logout/', logout_user, name = 'logout'),
    path('car-details/<int:car_id>/', car_details, name="car-details"),
    path('favourite-specific-car/<int:car_id>/', favourite_specific_car, name='favourite-specific-car'),
    path('favourites/', favourites, name='favourites'),
    path('delete-car-from-favourites/<int:item_id>/', delete_car_from_favourites, name='delete-car-from-favourites')

]
