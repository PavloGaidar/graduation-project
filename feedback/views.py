from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from onlainshop.settings import EMAIL_HOST_USER
from .models import SendMail
# Create your views here.
def show_feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        order = request.POST.get('order')




        message_for_client = f"Vitaemo, {name}!\nThanks for the Review about the store:{order}"
        message_for_admin = f"Feedback from the client: {name}\nCustomer email: {email}\ncustomer feedback: {order}"

        check_email_user = send_mail(
            subject = "Онлайн магазин",
            message = message_for_client,
            from_email = EMAIL_HOST_USER,
            recipient_list = [email],
            fail_silently=False
        )

        check_email_admin = send_mail(
            subject = "Онлайн магазин",
            message = message_for_admin,
            from_email = EMAIL_HOST_USER,
            recipient_list = [EMAIL_HOST_USER],
            fail_silently=False
        )

        if check_email_admin and check_email_user:  
            SendMail.objects.create(name = name,mail=email,order=order)
            return redirect('feedbackapp/feedback.html')
    return render(request, 'feedbackapp/feedback.html')
