from django.shortcuts import render, HttpResponse,redirect

def root(request):
    return redirect("/users")

def index(request):
    return HttpResponse("placeholder for users to create a new user record")

def login(request):
    return HttpResponse("placeholder for users to log in")

def user_dis(request):
    return HttpResponse("placeholder to later display all the list of users")