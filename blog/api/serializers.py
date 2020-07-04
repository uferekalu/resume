from rest_framework.serializers import ModelSerializer

from blog.models import BlogPost


class BlogPostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            # 'id',
            'title',
            # 'slug',
            'content',
            'publish_date'
        ]

class BlogPostDetailSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish_date'
        ]

class BlogPostListSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'user',
            'title',
            'slug',
            'content',
            'publish_date'
        ]

