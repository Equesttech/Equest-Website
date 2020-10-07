from . import views
from django.urls import path
from django.urls import include


app_name = 'blog'

urlpatterns = [
    path('blog/', views.PostList.as_view(), name='blog'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('summernote/', include('django_summernote.urls')),


]