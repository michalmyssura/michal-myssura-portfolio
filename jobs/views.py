from django.shortcuts import render
from .models import Job
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


# Create your views here.

def home(request):
    jobs = Job.objects

    request.method == 'POST'
    name = request.POST.get('name', '')
    message = request.POST.get('message','')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone','')
    y = '\n'
    x = message + y + email+ y + phone
    print(name, email, message,phone)
    if name and message and email:

        try:
            send_mail(name, x, email, ['michalmyssura2@gmail.com'], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request, 'jobs/index.html', {'jobs': jobs})
    else:
        return render(request,'jobs/index.html',{'jobs':jobs})



