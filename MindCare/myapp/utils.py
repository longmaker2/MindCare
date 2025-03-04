from django.core.mail import send_mail
from django.conf import settings
from googletrans import Translator


def send_email_async(subject, message, recipient_email):
    print(f"📧 Sending email to {recipient_email} with subject: {subject}")

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient_email],
            fail_silently=False  # Set to False to catch errors
        )
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Email sending failed: {e}")


def translate_text(text, dest_language='fr'):
    """Translate text to the specified destination language."""
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_language)
    return translated_text.text
