from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('edit_blog_post/<int:blog_id>/', views.edit_blog_post, name='edit_blog_post'),
]
