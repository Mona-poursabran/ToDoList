from django.db import models


class TODOList(models.Model):
    item = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.item} | {self.complete}'
