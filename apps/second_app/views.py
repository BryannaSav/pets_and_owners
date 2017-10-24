from __future__ import unicode_literals
from models import Pet
from ..login_app.models import User
from django.contrib import messages
from django.shortcuts import render, redirect


def dashboard(request):
    if "first_name" not in request.session:
        return redirect("/")
    context={
        'user':User.objects.get(id=request.session['id']).pets.all(),
        'other_users':User.objects.exclude(id=request.session['id'])
    }
    return render(request, "second_app/dashboard.html", context)

def addPet(request):
    return render(request, "second_app/add.html")

def createPet(request):
    # Pet.objects.create(name = request.POST["name"], pettype = request.POST["type"], users = request.POST["user"])

    results = Pet.objects.validate_review(request.POST)

    if results["status"] == True:
        for error in results["errors"]:
            messages.error(request, error)
        return redirect("/second_app/add_pet")
    else:
        test = User.objects.get(id = request.POST["user"])
        Pet.objects.create(name = request.POST["name"], pettype = request.POST["type"], users = test)
        return redirect("/second_app/dashboard")

def deletePet(request, id):
    Pet.objects.get(id=id).delete()
    return redirect("/second_app/dashboard")

def showUser(request, id):
    context={
        'user':User.objects.get(id=id),
        'pet':User.objects.get(id=id).pets.all()
    }
    return render(request, "second_app/show.html", context)

