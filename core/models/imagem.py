import uuid
from django.db import models

def upload_image_fomater(instance, filename):
    return f"{str(uuid.uuid4())}-{filename}"

class ImagemVeiculo(models.Model):
    image = models.ImageField(upload_to=upload_image_fomater, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)