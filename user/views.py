from django.shortcuts import render

# Create your views here.
def fnHome(request):
    return render(request,'home.html')
def fnSignin(request1):
    return render(request1,'signin.html')
def fnSignup(request2):
    return render(request2,'signup.html')
