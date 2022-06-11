from django.contrib import admin
from .models import Post
from django.contrib.sites.models import Site
from .models import Post, Ip


admin.site.register(Post)
admin.site.register(Ip)

admin.site.unregister(Site)
class SiteAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'domain')
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'domain')
    list_display_links = ('name',)
    search_fields = ('name', 'domain')
admin.site.register(Site, SiteAdmin)

