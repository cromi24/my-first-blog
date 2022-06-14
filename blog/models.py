from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum


def get_client_ip(self):
    x_forwarded_for = self.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = self.META.get('REMOTE_ADDR')
    return ip

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)

    @property
    def url(self):
        return '/post/{}/'.format(self.pk)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class PostViews(models.Model):

    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    date = models.DateField('Дата', default=timezone.now)
    datedViews = models.IntegerField('Просмотры', default=0)

    def  __str__(self):
        return self.post.title


class PostViewsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date', 'datedViews')
    search_fields = ('__str__', )


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            instance.profile.save()