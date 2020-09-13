from django.db import models

class UrlModel(models.Model):
    # Поле URlField проверяет введенный адрес на корректность формата
    original_url = models.URLField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.original_url