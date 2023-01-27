from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models
from django.template.loader import render_to_string
# Create your models here.


class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = 'M', "남성"
        FEMALE = 'F', "여성"

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(
        blank=True,
        max_length=13,
        validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")]
    )
    gender = models.CharField(
        blank=True,
        max_length=1,
        choices=GenderChoices.choices
    )
    avater = models.ImageField(
        blank=True,
        upload_to='accounts/avater/%Y/%m/%d',
        help_text="48px * 48px 크기의 png/jpeg 파일을 업로드해주세요."
    )

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