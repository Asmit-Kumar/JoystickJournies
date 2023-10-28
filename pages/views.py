from django.shortcuts import render, redirect

# Create your views here.
def landingpage(request, *args, **kwargs):
    my_dict = {}
    if request.user.is_authenticated:
        return redirect('home/')
    return render(request, 'pages/homeview.html', my_dict)

def home(request):
    dict = {}
    return render(request, 'pages/home.html', dict)

def About(request):
    return render(request, 'pages/about.html', {})
