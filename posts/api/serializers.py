from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from posts.models import Post


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'publish']


class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name="posts-api:detail",
        lookup_field="slug"
    )
    delete_url = HyperlinkedIdentityField(
        view_name="posts-api:delete",
        lookup_field="slug"
    )
    class Meta:
        model = Post
        fields = ['url', 'user', 'title', 'content', 'publish', 'delete_url']


class PostDetailSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name="posts-api:detail",
        lookup_field="slug"
    )
    class Meta:
        model = Post
        fields = ['id', 'url', 'user', 'title', 'content', 'publish']