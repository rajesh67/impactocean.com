from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from apps.webapp.models import Contact


def home(request):
	return render(request, 'web/index.html',{})

@csrf_exempt
def contact(request):
	if request.method=='POST':
		name=request.POST.get('name')
		phone=request.POST.get('phone')
		email=request.POST.get('email')
		message=request.POST.get('message')

		contact=Contact.objects.create(name=name,phone=phone,email=email,message=message)
		data={'status':'success'}

		subject = 'Thank you for registering to our site'
		message = ' it  means a world to us '
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [email,]

		send_mail( subject, message, email_from, recipient_list )
		return JsonResponse(data)
