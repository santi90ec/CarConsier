from django.shortcuts import render, redirect
from .models import State, Model, Brand,Customer,Employee,Address,Vehicle,Item
from session.models import User
from django.contrib import messages

def state_form(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id'])
    }
    return render(request, 'state.html',context)


def state_view(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "all_the_states": State.objects.order_by("name")
    }
    return render(request, 'state_view.html', context)


def state_edit(request,number):
    if 'session_id' not in request.session:
        return redirect('/state_edit')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "this_state": State.objects.get(id=number)
    }  
    return render(request,"state_edit.html",context)

def state_record(request):
    if request.method == 'POST':
        errors = State.objects.state_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/state_form')
        else:
            stateRecord = State.objects.create(name = request.POST['name'])
            stateRecord.save()
    return redirect('/state_view')

def state_update(request):
    if request.method == 'POST':
        errors = State.objects.state_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect(request.POST['state_id']+'/state_edit')
        else:
            this_state = State.objects.get(id = request.POST['state_id'])
            this_state.name = request.POST['name']
            this_state.save()
    return redirect('/state_view')







def model_form(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id'])
    }
    return render(request, 'model.html',context)

def model_view(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "all_the_models": Model.objects.filter(state=1).order_by("name")
    }
    return render(request, 'model_view.html', context)

def model_delete(request,number):
    if 'session_id' not in request.session:
        return redirect('/')
    this_model=Model.objects.get(id=number)
    this_model.state = State.objects.get(id = 2)
    this_model.save()
    return redirect('/model_view')

def model_edit(request,number):
    if 'session_id' not in request.session:
        return redirect('/model_edit')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "this_model": Model.objects.get(id=number)
    }  
    return render(request,"model_edit.html",context)

def model_record(request):
    if request.method == 'POST':
        errors = Model.objects.model_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/model_form')
        else:
            modelRecord = Model.objects.create(name = request.POST['name'],
            state = State.objects.get(id = 1))
            modelRecord.save()
    return redirect('/model_view')

def model_update(request):
    if request.method == 'POST':
        errors = Model.objects.model_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect(request.POST['model_id']+'/model_edit')
        else:
            this_model = Model.objects.get(id = request.POST['model_id'])
            this_model.name = request.POST['name']
            this_model.save()
    return redirect('/model_view')




def brand_form(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id'])
    }
    return render(request, 'brand.html',context)

def brand_view(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "all_the_brands": Brand.objects.filter(state=1).order_by("name")
    }
    return render(request, 'brand_view.html', context)

def brand_delete(request,number):
    if 'session_id' not in request.session:
        return redirect('/')
    this_brand=Brand.objects.get(id=number)
    this_brand.state = State.objects.get(id = 2)
    this_brand.save()
    return redirect('/brand_view')

def brand_edit(request,number):
    if 'session_id' not in request.session:
        return redirect('/brand_edit')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "this_brand": Brand.objects.get(id=number)
    }  
    return render(request,"brand_edit.html",context)

def brand_record(request):
    if request.method == 'POST':
        errors = Brand.objects.brand_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/brand_form')
        else:
            brandRecord = Brand.objects.create(name = request.POST['name'],
            state = State.objects.get(id = 1))
            brandRecord.save()
    return redirect('/brand_view')

def brand_update(request):
    if request.method == 'POST':
        errors = Brand.objects.brand_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect(request.POST['brand_id']+'/brand_edit')
        else:
            this_brand = Brand.objects.get(id = request.POST['brand_id'])
            this_brand.name = request.POST['name']
            this_brand.save()
    return redirect('/brand_view')




def employee_form(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id'])
    }
    return render(request, 'employee.html',context)

def employee_view(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "all_the_employees": Employee.objects.filter(state=1).order_by("last_name","first_name")
    }
    return render(request, 'employee_view.html', context)

def employee_delete(request,number):
    if 'session_id' not in request.session:
        return redirect('/')
    this_employee=Employee.objects.get(id=number)
    this_employee.state = State.objects.get(id = 2)
    this_employee.save()
    return redirect('/employee_view')

def employee_edit(request,number):
    if 'session_id' not in request.session:
        return redirect('/employee_edit')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "this_employee": Employee.objects.get(id=number)
    }  
    return render(request,"employee_edit.html",context)

def employee_record(request):
    if request.method == 'POST':
        errors = Employee.objects.employee_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/employee_form')
        else:
            employeeRecord = Employee.objects.create(first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            phone = request.POST['phone'],
            email = request.POST['email'],
            state = State.objects.get(id = 1))
            employeeRecord.save()
    return redirect('/employee_view')

def employee_update(request):
    if request.method == 'POST':
        errors = Employee.objects.employee_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect(request.POST['employee_id']+'/employee_edit')
        else:
            this_employee = Employee.objects.get(id = request.POST['employee_id'])
            this_employee.first_name = request.POST['first_name']
            this_employee.last_name = request.POST['last_name']
            this_employee.phone = request.POST['phone']
            this_employee.email = request.POST['email']
            this_employee.save()
    return redirect('/employee_view')







def address_form(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id'])
    }
    return render(request, 'address.html',context)

def address_view(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "all_the_addresss": Address.objects.filter(state=1).filter(user=User.objects.get(id = request.session['session_id'])).order_by("decription","reference")
    }
    return render(request, 'address_view.html', context)

def address_delete(request,number):
    if 'session_id' not in request.session:
        return redirect('/')
    this_address=Address.objects.get(id=number)
    this_address.state = State.objects.get(id = 2)
    this_address.save()
    return redirect('/address_view')

def address_edit(request,number):
    if 'session_id' not in request.session:
        return redirect('/address_edit')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "this_address": Address.objects.get(id=number)
    }  
    return render(request,"address_edit.html",context)

def address_record(request):
    if request.method == 'POST':
        errors = Address.objects.address_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/address_form')
        else:
            addressRecord = Address.objects.create(latitude = request.POST['latitude'],
            longitude = request.POST['longitude'],
            decription = request.POST['decription'],
            reference = request.POST['reference'],
            user = User.objects.get(id = request.session['session_id']),
            state = State.objects.get(id = 1))
            addressRecord.save()
    return redirect('/address_view')

def address_update(request):
    if request.method == 'POST':
        errors = Address.objects.address_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect(request.POST['address_id']+'/address_edit')
        else:
            this_address = Address.objects.get(id = request.POST['address_id'])
            this_address.latitude = request.POST['latitude']
            this_address.longitude = request.POST['longitude']
            this_address.decription = request.POST['decription']
            this_address.reference = request.POST['reference']
            this_address.save()
    return redirect('/address_view')






def vehicle_form(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "all_the_brands": Brand.objects.filter(state=1).order_by("name"),
        "all_the_models": Model.objects.filter(state=1).order_by("name")
    }
    return render(request, 'vehicle.html',context)

def vehicle_view(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "all_the_vehicles": Vehicle.objects.filter(state=1).filter(user=User.objects.get(id = request.session['session_id'])).order_by("decription","plate"),
        "all_the_brands": Brand.objects.filter(state=1).order_by("name"),
        "all_the_models": Model.objects.filter(state=1).order_by("name")
    }
    return render(request, 'vehicle_view.html', context)

def vehicle_delete(request,number):
    if 'session_id' not in request.session:
        return redirect('/')
    this_vehicle=Vehicle.objects.get(id=number)
    this_vehicle.state = State.objects.get(id = 2)
    this_vehicle.save()
    return redirect('/vehicle_view')

def vehicle_edit(request,number):
    if 'session_id' not in request.session:
        return redirect('/vehicle_edit')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "this_vehicle": Vehicle.objects.get(id=number),
        "all_the_brands": Brand.objects.filter(state=1).order_by("name"),
        "all_the_models": Model.objects.filter(state=1).order_by("name")
    }  
    return render(request,"vehicle_edit.html",context)

def vehicle_record(request):
    if request.method == 'POST':
        errors = Vehicle.objects.vehicle_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/vehicle_form')
        else:
            vehicleRecord = Vehicle.objects.create(plate = request.POST['plate'],
            year = request.POST['year'],
            decription = request.POST['decription'],
            brand = Brand.objects.get(id = request.POST['brand']),
            model = Model.objects.get(id = request.POST['model']),
            user = User.objects.get(id = request.session['session_id']),
            state = State.objects.get(id = 1))
            vehicleRecord.save()
    return redirect('/vehicle_view')

def vehicle_update(request):
    if request.method == 'POST':
        errors = Vehicle.objects.vehicle_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect(request.POST['vehicle_id']+'/vehicle_edit')
        else:
            this_brand = Brand.objects.get(id = request.POST['brand'])
            this_model = Model.objects.get(id = request.POST['model'])
            this_vehicle = Vehicle.objects.get(id = request.POST['vehicle_id'])
            this_vehicle.plate = request.POST['plate']
            this_vehicle.year = request.POST['year']
            this_vehicle.decription = request.POST['decription']
            this_vehicle.brand = this_brand
            this_vehicle.model = this_model
            this_vehicle.save()
    return redirect('/vehicle_view')



def item_form(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id'])
    }
    return render(request, 'item.html',context)

def item_view(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "all_the_items": Item.objects.filter(state=1).order_by("name")
    }
    return render(request, 'item_view.html', context)

def item_delete(request,number):
    if 'session_id' not in request.session:
        return redirect('/')
    this_item=Item.objects.get(id=number)
    this_item.state = State.objects.get(id = 2)
    this_item.save()
    return redirect('/item_view')

def item_edit(request,number):
    if 'session_id' not in request.session:
        return redirect('/item_edit')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "this_item": Item.objects.get(id=number)
    }  
    return render(request,"item_edit.html",context)

def item_record(request):
    if request.method == 'POST':
        errors = Item.objects.item_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/item_form')
        else:
            itemRecord = Item.objects.create(name = request.POST['name'],
            price = request.POST['price'],
            state = State.objects.get(id = 1))
            itemRecord.save()
    return redirect('/item_view')

def item_update(request):
    if request.method == 'POST':
        errors = Item.objects.item_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect(request.POST['item_id']+'/item_edit')
        else:
            this_item = Item.objects.get(id = request.POST['item_id'])
            this_item.name = request.POST['name']
            this_item.price = request.POST['price']
            this_item.save()
    return redirect('/item_view')
