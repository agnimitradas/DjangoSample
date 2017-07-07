from django.contrib import admin
from .models import CommentsModel,PostsModel

admin.site.register(PostsModel)
admin.site.register(CommentsModel)
