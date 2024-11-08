from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.apps import apps
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, ServiceForm, OrderForm, ServiceStationForm, CarForm# Імпортуйте ваші форми
from .models import User, Car, Service, ServiceStation, Order

def display_all_tables(request):
    model_names = ['User', 'Service', 'ServiceStation', 'Order', 'Car']
    models = [apps.get_model('lab', model_name) for model_name in model_names]

    html = "<html><body><h1>Database Tables</h1>"
    html += '<h2>Add New Record</h2>'
    html += '<a href="/add/user"><button>Add User</button></a>'
    html += '<a href="/add/car"><button>Add Car</button></a>'
    html += '<a href="/add/service_station"><button>Add Service Station</button></a>'
    html += '<a href="/add/service"><button>Add Service</button></a>'
    html += '<a href="/add/order"><button>Add Order</button></a>'
    html += '<br><br>'

    for model in models:
        model_name = model._meta.verbose_name_plural.capitalize()
        html += f"<h2>{model_name}</h2><table border='1'><tr>"

        field_names = [field.name for field in model._meta.fields]
        for field_name in field_names:
            html += f"<th>{field_name}</th>"
        html += "<th>Actions</th></tr>"

        for obj in model.objects.all():
            html += "<tr>"
            for field_name in field_names:
                value = getattr(obj, field_name)
                html += f"<td>{value}</td>"
            # Додаємо кнопку видалення
            html += f'<td><a href="/delete/{model.__name__.lower()}/{obj.id}/"><button>Delete</button></a></td>'
            html += "</tr>"

        html += "</table><br>"

    html += "</body></html>"
    return HttpResponse(html)


# Додаємо новий метод для обробки форм
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_all_tables')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_all_tables')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})

def add_service_station(request):
    if request.method == 'POST':
        form = ServiceStationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_all_tables')
    else:
        form = ServiceStationForm()
    return render(request, 'add_service_station.html', {'form': form})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_all_tables')
    else:
        form = ServiceForm()
    return render(request, 'add_service.html', {'form': form})

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_all_tables')
    else:
        form = OrderForm()
    return render(request, 'add_order.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('display_all_tables')
    return render(request, 'confirm_delete.html', {'object_type': 'User'})

def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('display_all_tables')
    return render(request, 'confirm_delete.html', {'object_type': 'Car'})

def delete_service_station(request, station_id):
    station = get_object_or_404(ServiceStation, id=station_id)
    if request.method == 'POST':
        station.delete()
        return redirect('display_all_tables')
    return render(request, 'confirm_delete.html', {'object_type': 'Service Station'})

def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('display_all_tables')
    return render(request, 'confirm_delete.html', {'object_type': 'Service'})

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('display_all_tables')
    return render(request, 'confirm_delete.html', {'object_type': 'Order'})