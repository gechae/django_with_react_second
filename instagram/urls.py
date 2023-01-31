from django.contrib.auth.validators import UnicodeUsernameValidator
from django.urls import path, re_path

from instagram import views

# include에 한함 - url reverse(perfix) 역할(namespace)
app_name = 'instagram'

# username_regex = UnicodeUsernameValidator.regex.lstrip('^').strip('$')
# print(f'username_regex: {repr(username_regex)}')

urlpatterns = [
    path('', views.index, name='index'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/like/', views.post_like, name='post_like'),
    path('post/<int:pk>/unlike/', views.post_unlike, name='post_unlike'),
    #re_path(r'(?P<username>[\w.@+-]+' + username_regex +')/', views.user_page, name='user_page'),
    re_path(r'(?P<username>[\w.@+-]+)/$', views.user_page, name='user_page'),
]