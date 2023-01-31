from django.urls import path

from instagram import views

# include에 한함 - url reverse(perfix) 역할(namespace)
app_name = 'instagram'

urlpatterns = [
    path('post/new/', views.post_new, name='post_new')
]