from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        """해당 모델은 다른 모델에서 확장을 위해 사용되므로 DB에 나타나지 않게 해준다."""

        abstract = True
