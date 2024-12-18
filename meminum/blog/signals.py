import os
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from .models import Article
from django.conf import settings


@receiver(pre_delete, sender=Article)
def delete_article_image(sender, instance, **kwargs):
    
    if instance.image:
        image_path = instance.image.path
        if os.path.isfile(image_path):
            os.remove(image_path)


@receiver(post_save, sender=Article)
def update_article_image(sender, instance, created, **kwargs):
    
    if not created and instance.image:
        old_instance = Article.objects.get(pk=instance.pk)
        if old_instance.image and old_instance.image != instance.image:
            old_image_path = old_instance.image.path
            if os.path.isfile(old_image_path):
                os.remove(old_image_path)
