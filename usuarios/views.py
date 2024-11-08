from django.shortcuts import render



def profile(request):
    return render(request, 'usuarios/profile.html')