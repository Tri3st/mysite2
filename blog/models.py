from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    class Role(models.Model):
        ADMIN = 'A', 'Admin'
        USER = 'U', 'User'
        MOD = 'M', 'Moderator'
        GUEST = 'G', 'Guest'
        BLOCKED = 'B', 'Blocked'
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=255, blank=True)
    avatar = models.URLField(blank=True)
    role = models.CharField(max_length=1, default=Role.USER)

    def __str__(self):
        return self.user.get_username()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Category(models.Model):
        NEWS = 'NE', 'News'
        INTERESTING = 'IN', 'Interesting'
        TECH = 'TE', 'Tech'
        MUSIC = 'MU', 'Music'
        MOVIE = 'MO', 'Movie'
        VARIOUS = 'VA', 'Various'
    title = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=2, default=Category.NEWS)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ["-publish_date"]
