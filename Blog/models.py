from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter( statues = Post.Status.PUBLISHED)
    
    def __str__(self):
        return self.name

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"
    
    class Genre(models.TextChoices):
        SHOOTER = 'Shooter', 'Shooter'
        CHOICEBASED = 'Choice Matters', 'Choice Matters'
        ADVENTURE = 'Adventure', 'Adventure'
        STRATEGY = 'Strategy', 'Strategy'


    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250)
    author = models.CharField(max_length=50)
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    genres = models.CharField(max_length=100, choices=Genre.choices)
    status = models.CharField(max_length = 2, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields = ['-publish']),
            models.Index(fields=['genres']),
        ]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    
