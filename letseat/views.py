from django.shortcuts import render

def custom_404(request, exception=None):
    """
    Custom 404 view
    """
    print('IN CUSTOM 404')
    print('args: ', request)
    print('kwargs: ', exception)
    return render(request, '404.html', status=404)