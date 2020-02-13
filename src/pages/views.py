from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Hello world</h1>")
	my_context = {
		"name": "Hao Ping",
		"age": 23,
		"skill": ["Java", "Python", "C++"],
		"fact": True
	}


	return render(request, "home.html", my_context)

def course_view(request, *args, **kwargs):

	return render(request, "course.html", {})

def plan_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Hello world</h1>")
	return render(request, "plan.html", {})


