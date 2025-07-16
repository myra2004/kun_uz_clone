# news/signals.py
import json
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import ClockedSchedule, PeriodicTask
from news.models import News

logger = logging.getLogger(__name__)

@receiver(post_save, sender=News)
def schedule_news_publish(sender, instance, created, **kwargs):
    """
    Если новость создаётся с заполненным scheduled_at,
    то ставим одноразовую задачу активировать её по расписанию.
    """
    if created and instance.scheduled_at:
        schedule_time = instance.scheduled_at

        # Создаём clocked schedule
        schedule, _ = ClockedSchedule.objects.get_or_create(
            clocked_time=schedule_time,
        )

        task_name = f"publish_news_{instance.id}"

        # Проверим, чтобы не было дубликатов
        task, created = PeriodicTask.objects.get_or_create(
            name=task_name,
            defaults={
                "task": "news.tasks.publish_news",
                "clocked": schedule,
                "args": json.dumps([instance.id]),
                "one_off": True,
                "start_time": schedule_time,
            }
        )

        if created:
            logger.info(f"[SIGNAL] Scheduled 'publish_news' task for News {instance.id} at {schedule_time}")
        else:
            logger.info(f"[SIGNAL] Task already exists for News {instance.id}")
