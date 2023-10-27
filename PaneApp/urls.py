from django.urls import path
from PaneApp.views import *
from users.views import messages, delete_msg, new_message

app_name = 'PaneApp'


urlpatterns = [
    # Inicio
    path('', inicio, name='Inicio'),
    # Oportunidades
    path('desc/', oportunidades, name='Desc'),
    path('desc/new_desc/', agregar_desc, name='NewDesc'),
    path('desc/delete_desc/<int:pk>', DeleteDesc.as_view(), name='Deletedes'),
    path('desc/edit_/<desc_id>/', edit_desc, name='EditDesc'),
    # Posts
    path('pages/', posts, name='Posts'),
    path('pages/new_post/', agregar_post, name='NewPost'),
    path('pages/delete_post/<int:pk>', DeletePost.as_view(), name='DeletePost'),
    path('pages/edit_post/<post_id>/', edit_post, name='EditPost'),
    path('pages/<post_id>/', post_detail, name='PostDetail'),
    # About
    path('about/', about, name='About'),
    # Messages
    path('messages/', messages, name='Messages'),
    path('messages/delete/<msg_id>/', delete_msg, name='DeleteMsg'),
    path('messages/new_msg/', new_message, name='NewMsg'),
]