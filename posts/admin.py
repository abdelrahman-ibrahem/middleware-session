from django.contrib import admin

# Register your models here.
from posts.models import Post
@admin.register(Post)
class PostAdminView(admin.ModelAdmin):
    list_display = ('title', 'creation_date', )