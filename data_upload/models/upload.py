import os
from django.db import models
from django.utils import timezone
from django.conf import settings

# ===============================================
#                  UPLOAD
# ===============================================
class UploadManager(models.Manager):
    def __init__(self) -> None:
        super().__init__()


gender_choice = (('Male', 'Male'), ('Female', 'Female'))
class Upload(models.Model):
    full_name = models.CharField(max_length=120)
    age = models.CharField(max_length=120)
    gender = models.CharField(choices=gender_choice, max_length=120)
    brief_history = models.TextField()
    symptoms = models.CharField(max_length=120)
    clinical_diagnosis = models.CharField(max_length=120)
    file = models.FileField(upload_to='db-media-files/')
    creation_date = models.DateTimeField(default=timezone.now)
    
    uploads = UploadManager()

    def __str__(self):
        return str(self.pk)

    def getRootDir(self):
        """Getting root dir of job."""
        media_root = str(settings.MEDIA_ROOT)
        return os.path.join(media_root, f'{self.pk}')
