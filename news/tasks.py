# news/tasks.py
import logging
from celery import shared_task
from news.models import News

logger = logging.getLogger(__name__)

@shared_task
def publish_news(news_id:int):
    try:
        news = News.objects.get(id=news_id)
        news.is_active = True
        news.save()
        logger.info(f"[TASK] News {news_id} is now active (published)")
    except News.DoesNotExist:
        logger.warning(f"[TASK] News {news_id} does not exist")
    except Exception as e:
        logger.error(f"[TASK] Error publishing News {news_id}: {e}")