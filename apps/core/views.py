from django.shortcuts import render

def home(request):
    """
    Renders the landing page of the application.
    """
    return render(request, 'core/home.html')
