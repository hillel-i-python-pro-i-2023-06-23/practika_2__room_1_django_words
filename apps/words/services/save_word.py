import logging

from apps.words.models import GameWord

# from apps.words.services.generate_animals import generate_animals


def create_object_word(word: str) -> GameWord:
    return GameWord(
        name_of_gamer="Player",
        word=str(word),
    )


def check_word(word: str):
    word_clean = word.lower().strip()
    queryset_last_word = GameWord.objects.all().order_by("-created_at").first()
    queryset = GameWord.objects.all()
    flag_the_same_word = False

    if queryset_last_word is not None:
        for check_word in queryset:
            if check_word.word == word_clean:
                flag_the_same_word = True
                break

    if flag_the_same_word:
        return False

    if queryset_last_word is not None:
        word_last = queryset_last_word.word
        if word_last[-1] == word_clean[0]:
            return True
        else:
            return False
    else:
        return True


def save_word(word: str) -> None:
    logger = logging.getLogger("django")

    queryset = GameWord.objects.all()

    logger.info(f"Current amount of words before: {queryset.count()}")

    if check_word(word=word):
        new_word = create_object_word(word=word)
        new_word.save()

    logger.info(f"Current amount of words after: {queryset.count()}")
