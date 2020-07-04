from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q
from django.utils.safestring import mark_safe
from django.db.models.signals import pre_save
from markdown_deux import markdown
from .utils import get_read_time
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)
    
    def search(self, query):
        lookup = (
            Q(title__icontains=query) | 
            Q(content__icontains=query) | 
            Q(slug__icontains=query) | 
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(user__username__icontains=query)
        )
        return self.filter(lookup)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)
    
    def published(self):
        return self.get_queryset().published()
    
    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(
        upload_to=upload_location, 
        blank=True, 
        null=True, 
        width_field='width_field', 
        height_field='height_field'
        )
    upload = models.FileField(upload_to=upload_location, blank=True, null=True)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    draft = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']
    
    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    
    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"
    
    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = BlogPost.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

    if instance.content:
        html_string = instance.get_markdown()
        read_time_var = get_read_time(html_string)
        instance.read_time = read_time_var


pre_save.connect(pre_save_post_receiver, sender=BlogPost)