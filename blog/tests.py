from django.test import TestCase

# Create your tests here.

'''class Ip(models.Model): #таблица где будут ip для счетчика
    ip = models.CharField(max_length=45)
    day = date()
    datedIp = (ip, day)

    def __str__(self):
        return self.datedIp'''

'''views = models.ManyToManyField(Ip,related_name="post_views", blank=True)

    def views_counter(self):
        return self.views.count()'''

'''total_views = models.IntegerField(default=0)

def counter(self):
    self.total_views += 1
    return self.total_views

ip = get_client_ip(request)
    if PostViews.objects.filter(ip=ip, day=date.today()).exists():
        post.views.add(PostViews.objects.get(ip=ip))
    else:
        PostViews.objects.create(ip=ip)
        post.views.add(PostViews.objects.get(ip=ip))'''