import logging

from apps.words.models import GameWord


def delete_words() -> None:
    logger = logging.getLogger("django")

    queryset = GameWord.objects.all()
    logger.info(f"Current amount of words before: {queryset.count()}")

    queryset_for_delete = queryset

    total_deleted, details = queryset_for_delete.delete()
    logger.info(f"Total deleted: {total_deleted}, details: {details}")

    logger.info(f"Current amount of words after: {queryset.count()}")
