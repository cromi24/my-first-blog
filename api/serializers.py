from rest_framework import serializers
from blog.models import *

class PostSerializerDetail(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post

        fields = ['pk', 'url', 'title', 'published_date']

