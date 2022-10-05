from django.urls import path
from django.views.generic import TemplateView
from .views import TestView

app_name = "blog_app"

urlpatterns = [
    path('',TemplateView.as_view(template_name="blog_app/index.html")),
    path('test/',TestView.as_view(),name='nothig')
]