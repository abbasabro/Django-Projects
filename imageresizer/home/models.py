from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import os
# Create your models here.
class ImageModel(models.Model):
    original_image= models.ImageField(upload_to="images/")
    thumbnail_small=models.ImageField(upload_to="images/thumbnails",null=True,blank=True)
    thumbnail_medium=models.ImageField(upload_to="images/thumbnails",null=True,blank=True)
    thumbnail_large=models.ImageField(upload_to="images/thumbnails",null=True,blank=True)

@receiver(post_save,sender=ImageModel)
def create_thumbnail(sender,instance , created , **kwargs):
    if created:
        sizes = {
            "thumbnail_small":(100,100),
            "thumbnail_medium":(300,300),
            "thumbnail_large":(700,700),   
        }

        for fields , size in sizes.items():
            img = Image.open(instance.original_image)
            img = img.convert("RGB")
            img.thumbnail(size,Image.Resampling.LANCZOS)
            thumbnail_name , thumbnail_extension = os.path.split(instance.original_image.name)
            thumbnail_extension = thumbnail_extension.lower()
            thumbnail_name = f"{thumbnail_name}_{size[0]}x{size[1]}{thumbnail_extension}"
            thumbnail_path = f"thumnails/{thumbnail_name}"
            img.save(thumbnail_path, optimize=True, quality=95)
            setattr(instance,fields,thumbnail_path)

