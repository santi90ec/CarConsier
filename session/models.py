from django.db import models
from datetime import datetime, date, time, timedelta
import calendar
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
import re
import bcrypt

NUMBER_REGEX = re.compile(r'^[0-9]+\.[0-9]$')
NAMES_REGEX = re.compile(r'^[a-zA-Z ]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def user_validator(self, registerData):
        errors = {}
        if len(registerData['first_name']) < 2 or not NAMES_REGEX.match(registerData['first_name']) :
            errors['first_name'] = "First Name must be at least 2 characters (only letters accepted)"
        if len(registerData['last_name']) < 2 or not NAMES_REGEX.match(registerData['last_name']):
            errors['last_name'] = "Last name must be at least 2 characters (only letters accepted)"
        if len(registerData['phone']) < 2 :
            errors['phone'] = "Phone must be at least 2 characters"
        if len(registerData['level']) == 0 :
            errors['level'] = "Level must be at least 1 characters"
        if registerData['email']!=registerData['user_email']:
            if not EMAIL_REGEX.match(registerData['email']):   
                errors['email'] = "Invalid email address"
            else:        
                email_exist = User.objects.filter(email = registerData['email'])
                if len(email_exist) >= 1:
                    errors['duplicate'] = "Email already exists"
        if len(registerData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if registerData['confirm'] != registerData['password']:
            errors['confirm'] = "Password must match!"
        return errors

    def login_validator(self, loginData):
        errors = {}
        if not EMAIL_REGEX.match(loginData['email']):   
            errors['email'] = "Invalid email address"
        else:
            email_exist = User.objects.filter(email = loginData['email'])
            if len(email_exist) == 0:
                errors['notfound'] = "Email not found, register first"
            else:
                hashedPWD = email_exist[0]
                if not bcrypt.checkpw(loginData['password'].encode(), hashedPWD.password.encode()):
                    errors['notmatch'] = "Incorrect password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    level = models.IntegerField()
    password = models.CharField(max_length=100)
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"<Show objects: {self.first_name} {self.last_name} ({self.id})>"

