from rest_framework.viewsets import ModelViewSet
from .models import CommentsModel,PostsModel
from .serializers import PostsSerializers,CommentsSerializers

class PostsView(ModelViewSet):
    queryset = PostsModel.objects.all()
    serializer_class = PostsSerializers

class CommentsView(ModelViewSet):
    queryset = CommentsModel.objects.filter(comment_on=1)
    serializer_class = CommentsSerializers

    def get_comments(self,request):
        print(request)