from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_order_confirmation_email(username, user_email, order_id):
    
    send_mail(
        subject=f"تأكيد الطلب رقم #{order_id}",
        message=f"أهلاً {username}، تم استلام طلبك بنجاح! الإجمالي:",
        from_email="noreply@ecommerce.com",
        recipient_list=[user_email],
        fail_silently=False,
    )