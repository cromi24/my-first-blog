from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response
from .serializers import PostSerializerDetail, PopularPostSerializer

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

    queryset = Post.objects.all()
    views = PostViews.objects.get_queryset().order_by('id')
    serializer_class = PopularPostSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [renderers.JSONRenderer]

    def list(self, request):
        queryset = self.queryset
        views = self.views
        type = request.query_params.get('type', None)
        print('type2: ', type)

        popularset = views.filter(
            date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
            ).values('post_id',
            ).annotate(datedViews=Sum('datedViews')
            ).order_by('-datedViews')
        popular_id = popularset[0].get('post_id')
        queryset = queryset.filter(id=popular_id)
        queryset.views = popularset[0].get('datedViews')
        serializer = PopularPostSerializer(queryset, many=True)
        return Response({
            'data': serializer.data,
        })