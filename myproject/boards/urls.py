from . import views
from django.urls import path

app_name = 'boards'

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:id>/', views.board_topics, name='board_topics'),
    path('boards/<int:id>/new_topic/', views.new_topic, name='new_topic'),
]
