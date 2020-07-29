from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse as Response
from django.views.decorators.csrf import csrf_protect
from .validation import FormValidation

from .models import Email

# Create your views here.
def home(request):
    # print(request.headers)

    context = {
        'WEB': settings.DEVFOLIO_SETTINGS,
        'RATING_LIST': range(1,6),    # Skill rating max = 5
        }
    return render(request, 'index.html', context)

@csrf_protect
def send_mail(request):

    if request.method != "POST":
        return Response("Method Not Allowed!", status=405)

    # Validate form data
    form = FormValidation(request.POST)
    if not form.is_valid():
        return Response(form.errors.as_json(), status=400)

    # Get name, email, subject & message
    sender_email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    sender_name = request.POST.get('name')
    origin = request.headers.get('Origin')

    # Delete Email older than 100
    email_count = Email.objects.count()
    if email_count > 100:
        Email.objects[0].delete()

    try:
        email_data = Email(
        sender_name = sender_name,
        sender_email = sender_email,
        subject = subject,
        message = message,
        origin = origin,
        )

        email_data.save()
        return Response("OK")
    except Exception as e:
        print(e)
        return Response("Service Unavailable", status=503)



