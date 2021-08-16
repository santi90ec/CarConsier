from catalogue.views import employee_delete
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from session.models import User
from catalogue.models import Vehicle,Address,State,Item,Employee
import re

NUMBER_REGEX = re.compile(r'^[0-9]+\.[0-9]$')
NAMES_REGEX = re.compile(r'^[a-zA-Z ]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class OrderManager(models.Manager):
    def order_validator(self, registerData):
        errors = {}
        if len(registerData['date_collect']) == 0 :
            errors['date_collect'] = "Date Collect must to have a value"
        if len(registerData['time_collect']) == 0 :
            errors['time_collect'] = "Time Collect must to have a value"
        if len(registerData['address_collect']) == 0 :
            errors['address_collect'] = "Address Collect must to have a value"
        if len(registerData['date_delivery']) == 0 :
            errors['date_delivery'] = "Date Delivery must to have a value"
        if len(registerData['time_delivery']) == 0 :
            errors['time_delivery'] = "Time Delivery must to have a value"
        if len(registerData['address_delivery']) == 0 :
            errors['address_delivery'] = "Address Delivery must to have a value"
        if len(registerData['item_delivery']) == 0 :
            errors['item_delivery'] = "Item Delivery must to have a value"
        if len(registerData['decription']) < 1  or len(registerData['decription']) > 100:
            errors['decription'] = "Decription must be at least 2 characters"
        if len(registerData['vehicle']) == 0 :
            errors['vehicle'] = "Vehicle must to have a value"
        return errors

    def order_validator_partial(self, registerData):
        errors = {}
        if len(registerData['item_collect']) == 0 :
            errors['item_collect'] = "Item Collect must to have a value"
        if len(registerData['item_delivery']) == 0 :
            errors['item_delivery'] = "Item Delivery must to have a value"
        if len(registerData['employee']) == 0 :
            errors['employee'] = "Employee must to have a value"
        if len(registerData['state']) == 0 :
            errors['state'] = "State must to have a value"
        return errors

class OrderTracingManager(models.Manager):
    def order_tracing_validator(self, registerData):
        errors = {}
        if len(registerData['decription']) < 1  or len(registerData['decription']) > 100:
            errors['decription'] = "Decription must be at least 2 characters"
        return errors


class Order(models.Model):
    date_collect = models.DateTimeField()
    time_collect = models.CharField(max_length=20)
    address_collect = models.ForeignKey(Address, related_name="address_collect_order", on_delete=CASCADE)
    item_collect = models.ForeignKey(Item, related_name="item_collect_order", on_delete=CASCADE)
    date_delivery = models.DateTimeField()
    time_delivery = models.CharField(max_length=20)
    address_delivery = models.ForeignKey(Address, related_name="address_delivery_order", on_delete=CASCADE)
    item_delivery = models.ForeignKey(Item, related_name="item_delivery_order", on_delete=CASCADE)
    vehicle = models.ForeignKey(Vehicle, related_name="vehicle_order", on_delete=CASCADE)
    decription = models.CharField(max_length=100)		 
    employee = models.ForeignKey(Employee, related_name="employee_order", on_delete=CASCADE)
    user = models.ForeignKey(User, related_name="user_order", on_delete=CASCADE)
    state = models.ForeignKey(State, related_name="state_order", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OrderManager()

    def __repr__(self):
        return f"<Show objects: {self.decription} ({self.id})>"

class OrderTracing(models.Model):
    decription = models.CharField(max_length=100)		 
    order = models.ForeignKey(Order, related_name="order_order_tracing", on_delete=CASCADE)
    user = models.ForeignKey(User, related_name="user_order_tracing", on_delete=CASCADE)
    state = models.ForeignKey(State, related_name="state_order_tracing", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OrderTracingManager()

    def __repr__(self):
        return f"<Show objects: {self.decription} ({self.id})>"

