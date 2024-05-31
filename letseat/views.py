from django.shortcuts import render, get_object_or_404

def custom_page_not_found(request, exception):
    return render(request, "templates/404.html", {})
