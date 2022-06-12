from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response
from .serializers import PostSerializerDetail, PopularPostSerializer
from django.db.models import Sum

from blog.models import *


class PostsViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializerDetail
    permission_classes = [permissions.AllowAny]
    renderer_classes = [renderers.JSONRenderer]

    def list(self, request):

        RECORDS_LIMIT = 3

        queryset = self.queryset

        type = request.query_params.get('type', None)

        print('type: ', type)

        if type == 'random':
            queryset = queryset.order_by('?')
        else:
            queryset = queryset.order_by('-pk')

        queryset = queryset[:RECORDS_LIMIT]

        serializer = PostSerializerDetail(queryset, many=True)
        return Response({
            'data': serializer.data,
        })


class PopularPostViewSet(viewsets.ModelViewSet):

    popularSet = PostViews.objects.all()
    serializer_class = PopularPostSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [renderers.JSONRenderer]

    def popular(self, request):
        popularSet = self.popularSet
        type = request.query_params.get('type', None)
        print('type: ', type)

        if type == 'popular':
            popularSet = popularSet.filter(
            date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
                ).values('post_id', 'post_title', 'post_datedViews',
                ).annotate(datedViews=Sum('post_datedViews')
                ).order_by('-post_datedViews')
            popular = popularSet[:1]
            serializer = PopularPostSerializer(popular)
        else: return

        return Response({
            'data': serializer.data,
        })