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
            "about.html",
            {
                "about": about
            },
        )
