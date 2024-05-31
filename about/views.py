from django.shortcuts import render
from django.views import generic, View
from .models import About


class AboutPage(View):
    """
    Class based view to render About page
    """

    def get(self, request, *args, **kwargs):
        """
        View that renders about page
        """

        return render(
            request,
            "about.html"
        )


def custom_404(request, exception):
    """
    Custom 404 view
    """
    return render(request, '404.html')
