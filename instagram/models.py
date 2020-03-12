from django.conf import settings
from django.db import models

# from django.contrib.auth.models import User  # nice한 방법이 아님

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    # 고품질 이미지 : imagemagic과 같은 라이브러리 사용
    photo = models.ImageField(blank=True, upload_to="instagram/post/%Y/%m/%d")
    # upload_to에는 함수도 지정 가능.
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Custom object{self.id}"

    class Meta:
        ordering = ["-id"]


class Comment(models.Model):
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, limit_choices_to={"is_public": True}
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pass
