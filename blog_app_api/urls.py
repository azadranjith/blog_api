from django.urls import path

from .views import PostList, PostDetail

app_name = 'blog_app_apwi'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name = 'listcreate'),

]
