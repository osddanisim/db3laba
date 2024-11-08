from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    license_plate = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cars")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.license_plate})"

class ServiceStation(models.Model):
    station_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.station_name

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    station = models.ForeignKey(ServiceStation, on_delete=models.CASCADE, related_name="services")

    def __str__(self):
        return self.service_name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="orders")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="orders")
    order_date = models.DateTimeField()
    order_status = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.id} - {self.order_status}"
