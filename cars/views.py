from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator

def cars(request):
    cars = Car.objects.all()

    # Pagination
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    # Unique filter options
    model_search = Car.objects.order_by('model').values_list('model', flat=True).distinct()
    city_search = Car.objects.order_by('city').values_list('city', flat=True).distinct()
    year_search = Car.objects.order_by('-year').values_list('year', flat=True).distinct()
    body_search = Car.objects.order_by('body_style').values_list('body_style', flat=True).distinct()

    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_search': body_search,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    car = get_object_or_404(Car, pk=id)
    data = {
        'car': car,
    }
    return render(request, 'cars/car_detail.html', data)

def search(request):
    cars = Car.objects.all()

    # Keyword search
    keyword = request.GET.get('keyword')
    if keyword:
        cars = cars.filter(description__icontains=keyword)

    # Model filter
    model = request.GET.get('model')
    if model:
        cars = cars.filter(model__iexact=model)

    # City filter
    city = request.GET.get('city')
    if city:
        cars = cars.filter(city__iexact=city)

    # Year filter
    year = request.GET.get('year')
    if year:
        cars = cars.filter(year__exact=year)

    # Body style filter
    body_style = request.GET.get('body_style')
    if body_style:
        cars = cars.filter(body_style__iexact=body_style)

    # Price range filter
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price and max_price:
        cars = cars.filter(price__gte=min_price, price__lte=max_price)

    # Unique filter options for sidebar
    model_search = Car.objects.order_by('model').values_list('model', flat=True).distinct()
    city_search = Car.objects.order_by('city').values_list('city', flat=True).distinct()
    year_search = Car.objects.order_by('-year').values_list('year', flat=True).distinct()
    body_search = Car.objects.order_by('body_style').values_list('body_style', flat=True).distinct()

    # Pagination
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_search': body_search,
        'keyword': keyword,
        'model': model,
        'city': city,
        'year': year,
        'body_style': body_style,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'cars/search.html', data)
