from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Hello world</h1>") 
	return render(request, "home.html", {})

def course_view(request, *args, **kwargs):
	my_context = {
		"my_text": "This is my context",
		"my_number": 123, 
		"my_list": [1313, 4231, 312, "Abc"],
		"this_is_true ": True
	}
	return render(request, "course.html", my_context)

def plan_view(request, *args, **kwargs):
	# return HttpResponse("<h1>Hello world</h1>")
	return render(request, "plan.html", {})
