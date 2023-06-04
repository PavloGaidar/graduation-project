from django.shortcuts import render

# Create your views here.
def show_feedback(request):
    respose = render(request, "feedbackapp/feedback.html")
    return respose
