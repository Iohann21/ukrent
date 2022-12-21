
from django.urls import path
from . import views 

urlpatterns = [
   path('', views.home, name="home"),
   path('about.html/', views.about, name="about"),
   path('service.html/', views.service, name="service"),
   path('car.html/', views.car, name="car"),
   path('contact.html/', views.contact, name="contact"),
   path('booking.html/',views.booking, name="booking"),
   path('detail.html/', views.detail, name="detail"),
   path('team.html/', views.team, name="team"),
   path('testimonial/', views.testimonial, name="testimonial"),
   
]
