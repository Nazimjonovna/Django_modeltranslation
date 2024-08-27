from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Post(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('title'), max_length=200),
        content = models.TextField(_("content")),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/')
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title