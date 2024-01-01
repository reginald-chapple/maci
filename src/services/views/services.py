from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.decorators import member_required
from services.forms import ServiceForm, BookingForm, ServiceRequestForm
from services.models import Service, Booking

"""_summary_: view that returns all services
"""
def all(request):
    context ={}
    context["services"] = Service.objects.all()
    
    return render(request, "services/all.html", context)

"""_summary_: view that creates a service
"""
@login_required
@member_required
def create(request):
    context ={}
    form = ServiceForm(request.POST or None)
    
    if form.is_valid():
        c = form.save(commit=False)
        c.save()
        return redirect("home")
        
    context['form']= form
    return render(request, "services/create.html", context)

"""_summary_: view that returns a single service
"""
def details(request, id):
    context ={}
    context["service"] = Service.objects.get(id = id) 
       
    return render(request, "services/details.html", context)

@login_required
@member_required
def service_request(request, id):
    if request.user.client == None:
        return redirect('forbidden')
    
    if id == None:
        return redirect('not-found')
    
    service = Service.objects.get(id = id)
    
    if service == None:
        return redirect('not-found')
    
    context ={}
    form = ServiceRequestForm(request.POST or None)
    
    if form.is_valid():
        c = form.save(commit=False)
        c.status = 'pending'
        c.client = request.user
        c.service = service
        c.save()
        return redirect('home')
   
    context['form']= form
    return render(request, "services/request.html", context)    

# @login_required
# @client_required
# def book(request, id):
#     if request.user.client == None:
#         return redirect('forbidden')
    
#     if id == None:
#         return redirect('not-found')
    
#     service = Service.objects.get(id = id)
    
#     if service == None:
#         return redirect('not-found')
    
#     context ={}
#     form = BookingForm(request.POST or None)
#     schedules = Schedule.objects.filter(provider=service.provider)
    
#     if form.is_valid():
#         c = form.save(commit=False)
#         combined_datetime = datetime.combine(c.date.today(), c.start_time) + service.duration
#         c.client = request.user.client
#         c.is_open = True
#         c.end_time = combined_datetime.time()
#         c.service = { "id": service.pk, "name": service.name, "price_per_hour": service.price_per_hour }
#         c.status = "pending"
#         c.schedule = schedules.get(day=c.date.weekday())
#         c.save()
#         return redirect('home')
   
#     context['form']= form
#     context['schedules'] = schedules
#     return render(request, "services/book.html", context)