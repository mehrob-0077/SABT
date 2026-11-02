from django.db.models.signals import post_save
from django.dispatch import receiver

from .helpers import send_confirmation_email
from .models import CostumUser, EmailConfirmed


@receiver(post_save, sender=CostumUser)
def send_email_verify(sender, instance, created, **kwargs):
    if created and not instance.is_active:
        token = EmailConfirmed.objects.create(user=instance)
        send_confirmation_email(token)

