from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import student, exercise
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, "journal/index.html")

def login(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_password = request.POST.get("user_password")
        f = student.objects.all()
        f = list(f)
        user_exists = 0
        current_user_name = ""
        current_user_password = ""
        for i in f:
            if (str(user_name) == str(i.name)) and (str(user_password) == str(i.password)):
                user_exists = 1
                current_user_name = str(i.name)
                current_user_password = str(i.password)
        if user_exists == 1:
            url = reverse("journal:dashboard", kwargs={"user_name" : current_user_name})
            return redirect(url)
        else:
            m = "User Doesn't Exist"
            return render(request, "journal/login.html", {"message" : m})
    return render(request, "journal/login.html")

def signup(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_password = request.POST.get("user_password")
        f = student(name = user_name, password = user_password)
        f.save()
        return render(request, "journal/login.html")
    return render(request, "journal/signup.html")

def dashboard(request, user_name):
    if request.method == "POST":
        # Saving exercise in database
        f = exercise(user_name = user_name, exercise_name = request.POST.get("exercise"), sets = request.POST.get("sets"), reps = request.POST.get("reps"))
        f.save()
        exercises = exercise.objects.all()
        exercises = list(exercises)
        new_list = []
        for i in exercises:
            if str(i.user_name) == str(user_name):
                new_list.append(i) 
        return render(request, "journal/dashboard.html", {"name" : user_name, "message" : new_list})
    exercises = exercise.objects.all()
    exercises = list(exercises)
    new_list = []
    for i in exercises:
        if str(i.user_name) == str(user_name):
            new_list.append(i) 
    return render(request, "journal/dashboard.html", {"name" : user_name, "message" : new_list})

def delete_exercise(request):
    if request.method == "POST":
        user_name_1 = request.POST.get("user_name")
        exercise_name_1 = request.POST.get("exercise")
        exercises_to_delete = exercise.objects.get(user_name = user_name_1, exercise_name = exercise_name_1)
        exercises_to_delete.delete()

        exercises = exercise.objects.all()
        exercises = list(exercises)
        new_list = []
        for i in exercises:
            if str(i.user_name) == str(user_name_1):
                new_list.append(i) 
        return render(request, "journal/dashboard.html", {"name" : user_name_1, "message" : new_list})
