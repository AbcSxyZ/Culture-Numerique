from django import forms
from .models import Commentary
from captcha.fields import CaptchaField

class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["username", "comment"]
    captcha = CaptchaField()
