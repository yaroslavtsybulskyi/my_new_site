"""
This module defines the views for the Planet Express website.
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from .context import home_page_text, about_us_text, contact_details


def home_view(request: HttpRequest) -> HttpResponse:
    """
    View function for the homepage.
    :param request: The request object
    :return: The rendered homepage template with `home_page_text`.
    """
    return render(request, 'main/home.html', {'home_page_text': home_page_text})


def about_view(request: HttpRequest) -> HttpResponse:
    """
    View function for the About Us page.
    :param request: The request object.
    :return: The rendered about page template with `about_us_text`.
    """
    return render(request, 'main/about.html', {'about_us_text': about_us_text})


class ContactView(View):
    """
    Class-based view for the Contact Us page.
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Handles GET requests for the Contact page.
        :param request: The request object.
        :return: The rendered contact page template with `contact_details`.
        """

        return render(request, 'main/contact.html', {'contact_details': contact_details})


class ServiceView(View):
    """
    Class-based view for the Service page.
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        :param request: The request object.
        :return: The rendered services page with a filtered or full list of services.
        """
        query = request.GET.get('q', '')
        services = contact_details.get("services", [])

        if query:
            services = [service for service in services if query.lower() in service["name"].lower()]

        return render(request, 'main/services.html', {'services': services, 'query': query})
