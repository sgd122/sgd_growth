from django.core.validators import MinLengthValidator
from django.db import models

# 단어 번역관련
from django.utils.translation import gettext_lazy as _


# 하나의 Model은 하나의 DB Table에 매핑됩니다.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "d", _("Draft")
        PUBLISHED = "p", _("Published")

    title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(10),  # Callable Object
        ],
    )
    content = models.TextField()
    status = models.CharField(
        max_length=1,
        # choices=[("d", "Draft"), ("p", "Published")]
        choices=Status.choices,
        default=Status.DRAFT,
    )
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title