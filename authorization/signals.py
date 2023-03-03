from django.utils.translation import gettext as _

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

import os


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(
        reverse('authorization_password_reset:reset-password-request'), reset_password_token.key)
    recovery_url = 'https://example.com' + email_plaintext_message

    merge_data = {
        'recovery_url': recovery_url,
        'username': reset_password_token.user.username
    }
    html_body = render_to_string(
        'authorization/emails/password-reset.html', merge_data)

    message = EmailMultiAlternatives(
        subject=_('Recuperar senha'),
        body="mail testing",
        from_email=os.environ.get('EMAIL_HOST_USER'),
        to=[reset_password_token.user.email]
    )
    message.attach_alternative(html_body, "text/html")
    message.send(fail_silently=False)
