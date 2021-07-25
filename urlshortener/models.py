from django.db import models


class Shortener(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    long_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'
