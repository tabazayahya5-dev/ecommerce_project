import os
from celery import Celery

# تعيين إعدادات Django الافتراضية لبرنامج Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# استخدام إعدادات Django ببادئة CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# البحث تلقائياً عن الـ tasks في جميع تطبيقات Django المسجلة
app.autodiscover_tasks()