from django.conf.urls import url, include
from django.contrib import admin
from main import urls as main_urls
from main import views as main_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sites/', include(main_urls)),
    url(r'^get_comments/', include(main_view.CommentsView.get_comments(1,2))),
]
