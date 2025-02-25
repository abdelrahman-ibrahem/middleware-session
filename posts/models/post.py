from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=240)
    content = models.TextField()
    image = models.ImageField(
        upload_to='posts/images/',
        null=True,
        blank=True
    )
    creation_date = models.DateTimeField(
        auto_now_add=True
    )

