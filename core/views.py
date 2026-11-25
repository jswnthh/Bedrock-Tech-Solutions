from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


def home(request):
    sent = False

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        service = request.POST.get('service', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email:
            send_mail(
                subject=f'Website enquiry: {service or "General"}',
                message=f'Name: {name}\nEmail: {email}\nService: {service}\n\n{message}',
                from_email=None,
                recipient_list=[settings.ENQUIRY_EMAIL],
            )
            sent = True

    return render(request, 'core/home.html', {'sent': sent})
