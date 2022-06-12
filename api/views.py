from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response
from .serializers import PostSerializerDetail
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

    def popular(self):
        context = {}
        popular = PostViews.objects.filter(
            date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
                ).values('post_id', 'post_title'
                ).annotate(views=Sum('views')
                ).order_by('-views')[:1]

        context['popular'] = popular
        return Response(data=context, template_name=self.template_name )
