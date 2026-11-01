from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

def send_confirmation_email(request, token):
    link = request.build_absolute_uri(reverse("confirm_email", args=[token.token]))
    send_mail(
        subject="Please confirm your email",
        message=f"Confirm your email address: {link}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[token.user.email],
    )



