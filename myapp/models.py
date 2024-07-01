from django.db import models
from django.core.validators import FileExtensionValidator

class uploadFile(models.Model):
    file = models.FileField(
        upload_to='',
        validators=[FileExtensionValidator(['csv', 'json'])]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
