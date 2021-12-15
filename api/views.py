from .models import Tweet
from .serializers import TweetSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import status
from rest_framework.response import Response


class TweetListApiView(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer 
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ["username"]
 
    
    
    def list(self, request, *args, **kwargs):
            queryset = self.filter_queryset(self.get_queryset())
            if not queryset.exists():
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        
     
    

