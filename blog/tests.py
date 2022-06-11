from django.test import TestCase

# Create your tests here.
total_views = models.IntegerField(default=0)

def counter(self):
    self.total_views += 1
    return self.total_views