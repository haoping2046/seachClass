from django.shortcuts import render

# Create your views here.
from .models import Policy


# Create your views here.
def ME_policy_view(request):
    obj = Policy.objects.get(id=1)

    context = {
        'object': obj
    }
    return render(request, "MEngPolicy.html", context)

def MS_policy_view(request):
    obj = Policy.objects.get(id=2)

    context = {
        'object': obj
    }
    return render(request, "MSngPolicy.html", context)


