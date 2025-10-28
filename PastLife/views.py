from django.shortcuts import render
from PastLife import models

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

    return render(request, 'home.html')