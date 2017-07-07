from rest_framework import routers

from main import views

router = routers.DefaultRouter()
router.register(r'comments', views.CommentsView)
router.register(r'posts', views.PostsView)
#router.register(r'posts/comm', views.CommentsView.get_comments,base_name=views.CommentsView.get_comments)
urlpatterns = router.urls