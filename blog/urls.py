from django.urls import path

from blog.views import BlogView, BlogDetail, CommentCreateView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('blogdeteil/<slug:slug>/', BlogDetail.as_view(), name='blogdeteil'),
    path('com/<slug:slug>/', CommentCreateView.as_view(), name='com'),
]
