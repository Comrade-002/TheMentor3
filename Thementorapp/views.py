from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def starter(request):
    return render(request, 'starter-page.html')
def pricing(request):
    return render(request, 'pricing.html')
def courses(request):
    return render(request, 'courses.html')
def details(request):
    return render(request, 'course-details.html')
def events(request):
    return render(request, 'events.html')
def trainers(request):
    return render(request, 'trainers.html')
def contact(request):
    return render(request, 'contact.html')
