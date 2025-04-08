from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse


class AuthMiddleware:
    """
    Middleware that ensures only the root page, login, and register pages are public.
    All other pages are protected and redirect to login if not authenticated.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of URLs that are allowed to be accessed without authentication
        public_urls = ["/", "/login/", "/register/"]

        # If the requested path is in the public_urls list, allow the request
        if request.path in public_urls:
            response = self.get_response(request)
        else:
            # Check if the user is authenticated
            if not request.user.is_authenticated:
                # Redirect to login page if not authenticated
                return redirect("/login/")
            response = self.get_response(request)

        return response
