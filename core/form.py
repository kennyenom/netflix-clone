from django.forms import ModelForm
from .models import *

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        exclude = ['uuid']