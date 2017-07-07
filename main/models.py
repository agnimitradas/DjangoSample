from django.contrib.auth.models import User
from django.db import models


class PostsModel(models.Model):
    post_body = models.CharField(max_length=500)
    post_created_at = models.DateField(auto_now=True)
    post_created_by = models.ForeignKey(User,related_name="user")

    def __str__(self):
        return self.post_body


class CommentsModel(models.Model):
    comments_body = models.CharField(max_length=150)
    comments_created_at = models.DateField(auto_now=True)
    comment_on = models.ForeignKey(PostsModel, related_name="postsModel")


    def __str__(self):
        return self.comments_body