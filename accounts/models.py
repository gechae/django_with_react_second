from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
# Create your models here.


class User(AbstractUser):
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)

    def send_welcome_email(self):
        """ 검색 해보기
        django render_to_string
        """

        subject = render_to_string('accounts/welcome_email_subject.txt', {
            "user": self,
        })
        content = render_to_string('accounts/welcome_email_content.txt', {
            "user": self,
        })
        sender_email = settings.WELCOME_EMAIL_SENDER
        response = send_mail(subject, content, sender_email, [self.email], fail_silently=False)
        if response:
            print(f"이메일 전송완료,({self.email}: {response})")
        else:
            print(f"이메일 전송실패,({self.email}: {response})")