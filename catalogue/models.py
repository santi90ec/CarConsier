from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from session.models import User
import re

NUMBER_REGEX = re.compile(r'^[0-9]+\.[0-9]$')
NAMES_REGEX = re.compile(r'^[a-zA-Z ]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class StateManager(models.Manager):
    def state_validator(self, registerData):
        errors = {}
        if len(registerData['name']) < 2 or len(registerData['name']) > 100:
            errors['name'] = "Name must be at least 2 characters"
        return errors

class ModelManager(models.Manager):
    def model_validator(self, registerData):
        errors = {}
        if len(registerData['name']) < 2 or len(registerData['name']) > 100:
            errors['name'] = "Name must be at least 2 characters"
        return errors

class BrandManager(models.Manager):
    def brand_validator(self, registerData):
        errors = {}
        if len(registerData['name']) < 2 or len(registerData['name']) > 100:
            errors['name'] = "Name must be at least 2 characters"
        return errors


class CustomerManager(models.Manager):
    def customer_validator(self, registerData):
        errors = {}
        if len(registerData['first_name']) < 2 or not NAMES_REGEX.match(registerData['first_name']) or len(registerData['first_name']) > 100:
            errors['first_name'] = "First Name must be at least 2 characters (only letters accepted)"
        if len(registerData['last_name']) < 2 or not NAMES_REGEX.match(registerData['last_name']) or len(registerData['last_name']) > 100:
            errors['last_name'] = "Last name must be at least 2 characters (only letters accepted)"
        if len(registerData['phone']) < 2 or len(registerData['phone']) > 100:
            errors['phone'] = "Address name must be at least 2 characters"
        if not EMAIL_REGEX.match(registerData['email']) or len(registerData['email']) > 100:   
            errors['email'] = "Invalid email address"
        return errors

class EmployeeManager(models.Manager):
    def employee_validator(self, registerData):
        errors = {}
        if len(registerData['first_name']) < 2 or not NAMES_REGEX.match(registerData['first_name']) or len(registerData['first_name']) > 100:
            errors['first_name'] = "First Name must be at least 2 characters (only letters accepted)"
        if len(registerData['last_name']) < 2 or not NAMES_REGEX.match(registerData['last_name']) or len(registerData['last_name']) > 100:
            errors['last_name'] = "Last name must be at least 2 characters (only letters accepted)"
        if len(registerData['phone']) < 2 or len(registerData['phone']) > 100:
            errors['phone'] = "Address name must be at least 2 characters"
        if not EMAIL_REGEX.match(registerData['email']) or len(registerData['email']) > 100:   
            errors['email'] = "Invalid email address"
        return errors

class AddressManager(models.Manager):
    def address_validator(self, registerData):
        errors = {}
        if len(registerData['latitude']) < 1 or len(registerData['latitude']) > 100:
            errors['latitude'] = "Latitude must be at least 2 characters"
        if len(registerData['longitude']) < 1  or len(registerData['longitude']) > 100:
            errors['longitude'] = "Longitude must be at least 2 characters"
        if len(registerData['decription']) < 1  or len(registerData['decription']) > 100:
            errors['decription'] = "Decription must be at least 2 characters"
        if len(registerData['reference']) < 1 or len(registerData['reference']) > 100:
            errors['reference'] = "Reference must be at least 2 characters"
        return errors


class VehicleManager(models.Manager):
    def vehicle_validator(self, registerData):
        errors = {}
        if len(registerData['plate']) < 1 or len(registerData['plate']) > 20:
            errors['plate'] = "Plate must be at least 2 characters"
        if len(registerData['year']) < 1  or len(registerData['year']) > 4:
            errors['year'] = "Year must be at least 2 characters"
        if len(registerData['decription']) < 1  or len(registerData['decription']) > 100:
            errors['decription'] = "Decription must be at least 2 characters"
        if len(registerData['brand']) == 0 :
            errors['brand'] = "Brand must to have a value"
        if len(registerData['model']) == 0 :
            errors['model'] = "Model must to have a value"
        return errors

class ItemManager(models.Manager):
    def item_validator(self, registerData):
        errors = {}
        num=0
        if len(registerData['name']) < 2 or len(registerData['name']) > 100:
            errors['name'] = "Name must be at least 2 characters"
        if len(registerData['price']) == 0 :
            errors['price'] = "Price must to have a value"
        try:
            num = float(registerData['price'])
        except ValueError:
            errors['price'] = "Invalid price"
        return errors



class State(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = StateManager()

    def __repr__(self):
        return f"<Show objects: {self.name} ({self.id})>"

class Model(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, related_name="state_model", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ModelManager()

    def __repr__(self):
        return f"<Show objects: {self.name} ({self.id})>"

class Brand(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, related_name="state_brand", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BrandManager()

    def __repr__(self):
        return f"<Show objects: {self.name} ({self.id})>"

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)		
    email = models.CharField(max_length=100)
    state = models.ForeignKey(State, related_name="state_customer", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CustomerManager()

    def __repr__(self):
        return f"<Show objects: {self.first_name} {self.last_name} ({self.id})>"


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)		
    email = models.CharField(max_length=100)
    state = models.ForeignKey(State, related_name="state_employee", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EmployeeManager()

    def __repr__(self):
        return f"<Show objects: {self.first_name} {self.last_name} ({self.id})>"

class Address(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    decription = models.CharField(max_length=100)		
    reference = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name="user_address", on_delete=CASCADE)
    state = models.ForeignKey(State, related_name="state_address", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AddressManager()

    def __repr__(self):
        return f"<Show objects: {self.decription} {self.reference} ({self.id})>"

class Vehicle(models.Model):
    plate = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    decription = models.CharField(max_length=100)		
    brand = models.ForeignKey(Brand, related_name="brand_vehicle", on_delete=CASCADE)
    model = models.ForeignKey(Model, related_name="model_vehicle", on_delete=CASCADE)
    user = models.ForeignKey(User, related_name="user_vehicle", on_delete=CASCADE)
    state = models.ForeignKey(State, related_name="state_vehicle", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = VehicleManager()

    def __repr__(self):
        return f"<Show objects: {self.plate} {self.decription} ({self.id})>"

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()	
    state = models.ForeignKey(State, related_name="state_item", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()

    def __repr__(self):
        return f"<Show objects: {self.name} ({self.id})>"
