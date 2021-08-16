from django.shortcuts import render, redirect
from .models import Order,OrderTracing
from session.models import User
from catalogue.models import Address,Vehicle,State,Item,Employee
from django.contrib import messages

def order_form(request):
    if 'session_id' not in request.session:
        return redirect('/')
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "all_the_address_collects": Address.objects.filter(state=1).filter(user=User.objects.get(id = request.session['session_id'])).order_by("decription","reference"),
        "all_the_address_deliverys": Address.objects.filter(state=1).filter(user=User.objects.get(id = request.session['session_id'])).order_by("decription","reference"),
        "all_the_vehicles": Vehicle.objects.filter(state=1).filter(user=User.objects.get(id = request.session['session_id'])).order_by("decription","plate"),
        "all_the_item_deliverys": Item.objects.filter(state=1).order_by("name")
    }
    return render(request, 'order.html',context)

def order_view(request):
    if 'session_id' not in request.session:
        return redirect('/')
    userRecord=User.objects.get(id = request.session['session_id'])
    if userRecord.level == 2:
        print(userRecord.level)
        all_the_orders=Order.objects.filter(user=User.objects.get(id = request.session['session_id'])).order_by("date_collect","time_collect")
    else:
        print(userRecord.level)
        all_the_orders=Order.objects.order_by("date_collect","time_collect")
    context = {
        "userRecord": userRecord,
        "all_the_orders": all_the_orders,
        "all_the_address_collects": Address.objects.filter(state=1).filter(user=User.objects.get(id = request.session['session_id'])).order_by("decription","reference"),
        "all_the_address_deliverys": Address.objects.filter(state=1).filter(user=User.objects.get(id = request.session['session_id'])).order_by("decription","reference"),
        "all_the_vehicles": Vehicle.objects.filter(state=1).filter(user=User.objects.get(id = request.session['session_id'])).order_by("decription","plate"),
        "all_the_item_deliverys": Item.objects.filter(state=1).order_by("name")
    }
    return render(request, 'order_view.html', context)

def order_delete(request,number):
    if 'session_id' not in request.session:
        return redirect('/')
    this_order=Order.objects.get(id=number)
    this_order.state = State.objects.get(id = 2)
    this_order.save()
    return redirect('/order_view')

def order_edit(request,number):
    if 'session_id' not in request.session:
        return redirect('/order_edit')
    
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "this_order": Order.objects.get(id=number),
        "all_the_address_collects": Address.objects.filter(state=1).filter(user=User.objects.get(id = request.session['session_id'])).order_by("decription","reference"),
        "all_the_address_deliverys": Address.objects.filter(state=1).filter(user=User.objects.get(id = request.session['session_id'])).order_by("decription","reference"),
        "all_the_vehicles": Vehicle.objects.filter(state=1).filter(user=User.objects.get(id = request.session['session_id'])).order_by("decription","plate"),
        "all_the_item_deliverys": Item.objects.filter(state=1).order_by("name")
    }  
    return render(request,"order_edit.html",context)

def order_edit_update(request,number):
    if 'session_id' not in request.session:
        return redirect('/order_update')
    this_order = Order.objects.get(id = number)
    context = {
        'userRecord': User.objects.get(id = request.session['session_id']),
        "this_order": Order.objects.get(id=number),
        "all_the_address_collects": Address.objects.filter(state=1).filter(user=User.objects.get(id = request.session['session_id'])).order_by("decription","reference"),
        "all_the_address_deliverys": Address.objects.filter(state=1).filter(user=User.objects.get(id = request.session['session_id'])).order_by("decription","reference"),
        "all_the_vehicles": Vehicle.objects.filter(state=1).filter(user=User.objects.get(id = request.session['session_id'])).order_by("decription","plate"),
        "all_the_employees": Employee.objects.filter(state=1).order_by("last_name","first_name"),
        "all_the_item_collects": Item.objects.filter(state=1).order_by("name"),
        "all_the_item_deliverys": Item.objects.filter(state=1).order_by("name"),
        "all_the_states": State.objects.order_by("name"),
        "all_the_order_tracings": OrderTracing.objects.filter(state=1).filter(order=this_order).order_by("updated_at")
    }  
    return render(request,"order_update.html",context)


def order_record(request):
    if request.method == 'POST':
        errors = Order.objects.order_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/order_form')
        else:
            orderRecord = Order.objects.create(date_collect = request.POST['date_collect'],
            time_collect = request.POST['time_collect'],
            date_delivery = request.POST['date_delivery'],
            time_delivery = request.POST['time_delivery'],
            decription = request.POST['decription'],
            address_collect = Address.objects.get(id = request.POST['address_collect']),
            address_delivery = Address.objects.get(id = request.POST['address_delivery']),
            vehicle = Vehicle.objects.get(id = request.POST['vehicle']),
            employee= Employee.objects.get(id = 1),
            item_collect= Item.objects.get(id = 1),
            item_delivery= Item.objects.get(id = request.POST['item_delivery']),
            user = User.objects.get(id = request.session['session_id']),
            state = State.objects.get(id = 1))
            orderRecord.save()
    return redirect('/order_view')

def order_update(request):
    if request.method == 'POST':
        errors = Order.objects.order_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect(request.POST['order_id']+'/order_edit')
        else:
            this_item_delivery = Item.objects.get(id = request.POST['item_delivery'])
            this_address_collect = Address.objects.get(id = request.POST['address_collect'])
            this_address_delivery = Address.objects.get(id = request.POST['address_delivery'])
            this_vehicle = Vehicle.objects.get(id = request.POST['vehicle'])
            this_order = Order.objects.get(id = request.POST['order_id'])
            this_order.date_collect = request.POST['date_collect']
            this_order.time_collect = request.POST['time_collect']
            this_order.date_delivery = request.POST['date_delivery']
            this_order.time_delivery = request.POST['time_delivery']
            this_order.decription = request.POST['decription']
            this_order.address_collect = this_address_collect
            this_order.address_delivery = this_address_delivery
            this_order.vehicle = this_vehicle
            this_order.item_delivery = this_item_delivery
            this_order.save()
    return redirect('/order_view')


def order_update_update(request):
    if request.method == 'POST':
        errors = Order.objects.order_validator_partial(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect(request.POST['order_id']+'/order_edit_update')
        else:
            this_item_delivery = Item.objects.get(id = request.POST['item_delivery'])
            this_item_collect = Item.objects.get(id = request.POST['item_collect'])
            this_employee = Employee.objects.get(id = request.POST['employee'])
            this_state = State.objects.get(id = request.POST['state'])
            this_order = Order.objects.get(id = request.POST['order_id'])
            this_order.item_collect = this_item_collect
            this_order.item_delivery = this_item_delivery
            this_order.employee = this_employee
            this_order.state = this_state
            this_order.save()
    return redirect('/order_view')

def order_tracing_record(request):
    if request.method == 'POST':
        errors = OrderTracing.objects.order_tracing_validator(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect(request.POST['order_id']+'/order_update')
        else:
            orderTracingRecord = OrderTracing.objects.create(decription = request.POST['decription'],
            order = Order.objects.get(id = request.POST['order_id']),
            user = User.objects.get(id = request.session['session_id']),
            state = State.objects.get(id = 1))
            orderTracingRecord.save()
    return redirect(request.POST['order_id']+'/order_update')
