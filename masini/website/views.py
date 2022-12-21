from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})
    
def about(request):
    return render(request, 'about.html', {})

def service(request):
    return render(request, 'service.html', {})

def car(request):
    return render(request, 'car.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def booking(request):
    return render(request, 'booking.html', {})

def detail(request):
    return render(request, 'detail.html', {})

def team(request):
    return render(request, 'team.html', {})

def testimonial(request):
    return render(request, 'testimonial.html', {})
    