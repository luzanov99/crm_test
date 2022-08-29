from comments.models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        read_only_fields=('content_type', 'object_id')
        fields = '__all__'