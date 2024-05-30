from django.shortcuts import render


def pagenotfound(request, exception):
    """ Error 404 Handler """
    return render(request, "error/error404.html", status=404)
