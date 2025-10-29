from django.shortcuts import render
from PastLife import models
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        # Handle form submission logic here
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create a new contact message instance
        contact_message = models.ContactMessage(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )
        contact_message.save()

        # Send email notification
        send_mail(
            f"We have received your message, {first_name} {last_name}!",
            "We aim to respond within 24-48 hours.",
            email,
            [email],  # To customer email
            fail_silently=False,
        )
        send_mail(
            f"We have received a message from {first_name} {last_name}",
            message,
            email,
            ['austindylan0@gmail.com'],  # To our email
            fail_silently=False,
        )

    return render(request, 'home.html')