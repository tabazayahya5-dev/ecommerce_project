from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_order_confirmation_email(order_id, recipient_email):
    subject = f"تأكيد الطلب رقم #{order_id}"
    message = f"مرحباً،\n\nتم استلام طلبك رقم #{order_id} بنجاح.\nشكراً لتسوقك معنا!"
    
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[recipient_email], # بريد العميل الديناميكي
        fail_silently=False,
    )