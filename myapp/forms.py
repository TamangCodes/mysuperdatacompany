from django import forms
from .models import uploadFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = uploadFile
        fields = ['file']