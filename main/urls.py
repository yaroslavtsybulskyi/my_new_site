from django.urls import path

from main.views import home_view, about_view, ContactView, ServiceView

urlpatterns = [
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('services/', ServiceView.as_view(), name='services'),

]
