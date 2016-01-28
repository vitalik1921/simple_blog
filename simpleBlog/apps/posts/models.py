from django.db import models
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_delete
from tinymce.models import HTMLField
from . import utils
from . import signals


class Image(models.Model):
    Image = models.ImageField(upload_to='posts')
    ShortName = models.CharField(max_length=100, blank=True)
    Description = models.CharField(max_length=250, blank=True)

    def get_thumbnail_html(self):
        return '<a class="image-picker" href="{}" target="_blank"><img src="{}" alt="{}"/></a>' \
            .format(self.Image.url, utils.get_thumbnail_url(self.Image.url), self.Description)

    get_thumbnail_html.short_description = 'Image'
    get_thumbnail_html.allow_tags = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        if not self.ShortName:
            fragments = self.Image.name.split('.')
            if len(fragments) > 1:
                self.ShortName = slugify(fragments[0])
            else:
                self.ShortName = slugify(self.Image.name)

        super().save(force_insert, force_update, using, update_fields)


post_save.connect(signals.post_save_handler, sender=Image)
pre_delete.connect(signals.pre_delete_handler, sender=Image)


class Category(models.Model):
    """
    Category
    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('category', args={self.slug})

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    Post
    """
    title = models.CharField(max_length=160)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)
    content = HTMLField(blank=True)
    category = models.ForeignKey(Category)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
