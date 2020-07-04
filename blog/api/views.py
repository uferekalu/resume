from django.db.models import Q
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )

from blog.models import BlogPost
from .serializers import (
    BlogPostListSerializer, 
    BlogPostDetailSerializer,
    BlogPostCreateUpdateSerializer
    )

from .permissions import IsOwnerOrReadOnly

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

class BlogPostCreateAPIView(CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BlogPostDetailAPIView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailSerializer
    lookup_field = 'slug'

class BlogPostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class BlogPostDeleteAPIView(DestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailSerializer
    lookup_field = 'slug'

class BlogPostListAPIView(ListAPIView):
    serializer_class = BlogPostListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = BlogPost.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)|
                Q(user__first_name__icontains=query)|
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list

