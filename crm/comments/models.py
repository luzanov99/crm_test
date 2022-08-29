from django.db import models
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from users.models import User
# Create your models here.
class Comment(models.Model):
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='comment_user')
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/', blank=True)
    content_type = models.ForeignKey(ContentType, related_name="content_type_comment", on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')