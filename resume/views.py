from django.shortcuts import render
from django.conf import settings

# Create your views here.
def home(request):
    # print(request.headers)

    context = {
        'WEB': settings.DEVFOLIO_SETTINGS,
        'RATING_LIST': range(1,6),    # Skill rating max = 5
        }
    return render(request, 'index.html', context)
