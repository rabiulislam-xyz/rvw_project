from string import ascii_letters
from random import choice
from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField


def slug_uniquify(slug):
    qs = Post.objects.filter(slug=slug)
    if qs.exists():
        while True:
            slug = slug + '-' + choice(ascii_letters)
            if not qs.filter(slug=slug).exists():
                break
    return slug

def bangla_slugify(text):
    first_ten_word = text.split()[:10]
    slug = '-'.join(first_ten_word)
    unique_slug = slug_uniquify(slug)

    return unique_slug


class Post(models.Model):
    title    = models.CharField(max_length=200)
    slug     = models.SlugField(allow_unicode=True, blank=True)
    content  = RichTextField()
    created  = models.DateTimeField(auto_now=True)
    updated  = models.DateTimeField(auto_now_add=True)
    is_draft = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:
            slug = bangla_slugify(self.slug)
        else:
            slug = bangla_slugify(self.title)

        self.slug = slug
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created', '-updated']
