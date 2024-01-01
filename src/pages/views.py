from django.shortcuts import render, redirect

def home(request):
    context = {}
    # if request.user.is_authenticated and request.user.is_provider:
    #     friday = "Sunday"
    #     schedule = Schedule.objects.get(provider=request.user.provider, day=friday)
        
    #     print(schedule.get_available_hours())
    #     context["schedules"] = request.user.provider.schedules.all()
    template_name='pages/home.html'
    return render(request, template_name, context)

