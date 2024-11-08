from django import forms
from .models import User, Car, ServiceStation, Service, Order

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class ServiceStationForm(forms.ModelForm):
    class Meta:
        model = ServiceStation
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
