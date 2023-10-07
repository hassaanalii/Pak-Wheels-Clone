from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.db import connections
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, FavoriteForm
from .models import CarsTable, Favorite
from .serializers import MyModelSerializer, FavouriteSerializer
from django.core.paginator import Paginator
from rest_framework import status

# Define a filter dictionary to map user input to query conditions
filter_conditions = {}

# Define constants for URL names
LOGIN_URL_NAME = 'login'
FAVOURITES_URL_NAME = 'favourites'
FAV_SPECIFIC_CAR_URL_NAME = 'favourite_specific_car'
HOME_PAGE_URL_NAME = 'home_page'

@api_view(['GET'])
@login_required(login_url='login')
def home_page(request):
    location = request.GET.get("location")
    model = request.GET.get("model")
    transmission = request.GET.get("transmission")

    filter_conditions = {}  # Initialize the filter conditions dictionary

    # Apply filters based on user input
    if location:
        filter_conditions['location'] = location

    if model:
        if "-" in model:  
            start_year, end_year = map(int, model.split("-"))
            filter_conditions['model__range'] = (start_year, end_year)
        else: 
            filter_conditions['model'] = model

    if transmission:
        filter_conditions['transmission'] = transmission

    cars = CarsTable.objects.filter(**filter_conditions)

    paginator = Paginator(cars, 30)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    serialized_data = MyModelSerializer(page, many=True)
    user_favorites = Favorite.objects.filter(user=request.user, is_deleted=False).values_list('car_id', flat=True)

    return render(request, 'car_data.html', context={'serialized_data': serialized_data.data, "page": page, 'user_favs': user_favorites})

@api_view(['GET'])
def car_details(request, car_id):
    car = get_object_or_404(CarsTable, id=car_id)
    return render(request, 'car_details.html', {'car': car})

def login_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get("phone-number")
        password = request.POST.get("password")

        # Authenticate using the 'phone_number' field
        user = authenticate(request, phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            return redirect(HOME_PAGE_URL_NAME)
        else:
            messages.info(request, 'Phone number or Password is incorrect!')
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect(LOGIN_URL_NAME)

def delete_car_from_favourites(request, item_id):
    favorite = get_object_or_404(Favorite, id=item_id, user=request.user)
    favorite.soft_delete()
    return redirect(HOME_PAGE_URL_NAME)

@api_view(['POST', 'GET'])
@login_required(login_url=LOGIN_URL_NAME)
def favourite_specific_car(request, car_id):
    if request.method == 'POST':
        form = FavoriteForm(request.POST)
        if form.is_valid():
            car = get_object_or_404(CarsTable, pk=car_id)
            data = {
                "user": request.user.pk,
                "car": car.pk,
                "notes": request.data.get("notes"),
                "rating": request.data.get("rating")
            }
            serializer = FavouriteSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=request.user, car=car)
                return redirect(HOME_PAGE_URL_NAME)
            else:
                return render(request, 'fav-specific-car.html', {'form': form, 'error': serializer.errors})
        else:
            return render(request, 'fav-specific-car.html', {'form': form})
    else:
        car = get_object_or_404(CarsTable, pk=car_id)
        existing_favorite = Favorite.objects.filter(car=car, user=request.user, is_deleted=False).first()

        if existing_favorite:
            delete_fav_url = reverse('delete-car-from-favourites', kwargs={'item_id': existing_favorite.id})        
            return redirect(delete_fav_url)
        else:
            form = FavoriteForm()

    return render(request, 'fav-specific-car.html', {'form': form})

def registration_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(LOGIN_URL_NAME)

    context = {'form': form}
    return render(request, 'register.html', context)

@login_required(login_url='login')
def favourites(request):
    cars_of_specific_user = Favorite.objects.filter(user_id=request.user, is_deleted=False)
    car_details = []

    for item in cars_of_specific_user:
        one_car = CarsTable.objects.get(pk=item.car_id)
        car_details.append({'car': one_car, 'favourite': item})

    return render(request, 'myfavs.html', {'favs': car_details})

def landing_page(request):
    return render(request, 'landingpage.html')
