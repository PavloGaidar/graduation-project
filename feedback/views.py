from django.shortcuts import render
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def show_feedback(request):
    respose = render(request, "feedbackapp/feedback.html")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        send_mail(subject= 'Feedback', message= f'Name: {name}  Email: {email}\nFeedback: {feedback}', from_email= 'settings.EMAIL_HOST_USER', recipient_list= ['bytebliss7@gmail.com'], fail_silently=False,
        )
        return respose
    return respose
