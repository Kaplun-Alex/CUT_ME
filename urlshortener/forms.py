from datetime import timedelta
from django import forms
from django.utils import timezone

from .models import Shortener
from .utils import create_shortened_url


class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(
        widget=forms.URLInput(attrs={"class": "form-control form-control-lg", "placeholder": "GIVE ME URL"})
    )

    class Meta:
        model = Shortener
        fields = ('long_url',)

    def save(self, commit=True, *args, **kwargs):
        long_url = self.cleaned_data['long_url']
        old_link = Shortener.objects.filter(long_url=long_url).last()

        if old_link:
            if old_link.updated_at + timedelta(hours=1) < timezone.now():
                old_link.short_url = create_shortened_url(old_link)
                old_link.save()

            self.instance = old_link

        else:
            self.instance.short_url = create_shortened_url(self.instance)
            super().save(*args, **kwargs)

        return self.instance

