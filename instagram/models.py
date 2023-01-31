import re

from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    photo = models.ImageField(upload_to='instagram/post/%Y/%m/%d')
    caption = models.CharField(
        max_length=500
    )
    tag_set = models.ManyToManyField(
        'Tag',
        blank=True
    )
    location = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.caption

    def extract_tag_list(self):
        tag_name_list = re.findall(r"#([a-zA-Z\dr-힣]+)", self.caption)
        tag_list = list()
        for tag_name in tag_name_list:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)
        return tag_list

    """
    어떠한 모델에 대해서 detail 뷰를 만들게 되면 get_absolute_url() 멤버 함수를 무조건 선언
    resolve_url(모델 인스턴스), redirect(모델 인스턴스) 를 통해서 모델 인스턴스의 get_absolute_url() 함수를 자동으로 호출
    resolve_url() 함수는 가장 먼저 get_absolute_url 함수의 존재 여부를 체크하고, 존재하면 호출하며 그 리턴값으로 URL을 사용
    """
    def get_absolute_url(self):
        return reverse("instagram:post_detail", args=[self.pk])


class Tag(models.Model):
    name = models.CharField(
        max_length=60,
        unique=True
    )

    def __str__(self):
        return self.name