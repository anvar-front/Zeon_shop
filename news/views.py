from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News
from .pagination import PaginationHandlerMixin
from .serializers import NewsSerializer


class BasicPagination(PageNumberPagination):
    """
    Пагинация
    """
    page_size = 8
    page_size_query_param = 'limit'
    max_page_size = 100


class NewsAPIView(APIView, PaginationHandlerMixin):
    """
    Представление для новостей
    """
    pagination_class = BasicPagination
    serializer_class = NewsSerializer

    def get(self, request, format=None, *args, **kwargs):
        news = News.objects.all()
        page = self.paginate_queryset(news)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)
        else:
            serializer = self.serializer_class(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
