from django.test import TestCase

# Create your tests here.
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def passReset_email(request):
    subject = request.POST.get('subject', 'Password reset on cromi24 blog')
    message = request.POST.get('message', 'templates/registration/password_reset_email.html')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, [''])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/templates/registration/password_reset_done.html')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')